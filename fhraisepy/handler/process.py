import ctypes
import inspect
from enum import Enum
from pathlib import Path
from time import time
from typing import Callable, Dict

import brushface
import cv2
import numpy as np

from fhraisepy import lib, symbols
from fhraisepy.logger import Logger
from fhraisepy.native.libfhraisepy import *


class ProcessType(Enum):
    Register = "r"
    Verify = "v"


frame_converters: Dict[str, Callable[[np.ndarray, int], np.ndarray]] = {
    "Rgb": lambda frame, width: cv2.cvtColor(
        frame.reshape((-1, width, 3)), cv2.COLOR_RGB2BGR
    ),
    "Bgr": lambda frame, width: frame.reshape((-1, width, 3)),
}
"""
将任意格式的帧转换为 BGR 3 维数组。

函数的第一个参数是帧的原始数据，第二个参数是帧的宽度。
"""

db_path = Path("images")
confidence_threshold = 0.8
register_max_frame = 5
timeout_seconds = 30

current_user_id: str | None = None
process_type: ProcessType | None = None
start_time: float | None = None
processed_frame = 0
busy = False


def cleanup():
    global current_user_id, process_type, start_time, processed_frame, busy

    current_user_id = None
    process_type = None
    start_time = None
    processed_frame = 0
    busy = False


def on_data(
    frame_format: str,
    width: int,
    result: ctypes.POINTER(libfhraisepy_kref),
):
    def void(ref: libfhraisepy_kref):
        global busy

        logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

        busy = False

        result.contents = ref
        logger.debug(f"Result is set to {ref}.")

    def normal():
        global processed_frame
        processed_frame += 1

        if processed_frame == register_max_frame:
            cleanup()

            brushface.update_datastore(db_path)

            return void(lib.Message.Result.Success._instance())

        return void(lib.Message.Result.Next._instance())

    @ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int)
    def send_frame(data: int, size: int):
        logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

        byte_ptr = ctypes.cast(data, ctypes.POINTER(ctypes.c_byte))

        frame = np.array(byte_ptr[:size]).astype(np.uint8)

        logger.debug(f"Received frame {type(frame)} with size {size}.")

        if frame_format not in frame_converters:
            logger.error(f"Converter for frame format {frame_format} not found.")
            return void(lib.Message.Result.InternalError._instance())

        converter = frame_converters[frame_format]

        logger.debug(f"Converter {converter.__name__} is used for this frame.")

        frame = converter(frame, width)
        faces = brushface.extract_faces(frame, enforce_detection=False)
        faces.sort(key=lambda x: x["face_area"]["confidence"], reverse=True)

        if len(faces) == 0:
            logger.error("No faces detected.")
            return void(lib.Message.Result.NoFaces._instance())

        face = faces[0]

        confidence = face["face_area"]["confidence"]
        if confidence < confidence_threshold:
            logger.error(
                f"Face confidence is too low: {confidence}, threshold is {confidence_threshold}."
            )
            return void(lib.Message.Result.LowResolution._instance())

        if process_type == ProcessType.Register:
            cv2.imwrite(
                str(db_path / current_user_id / f"{processed_frame}.jpg"),
                face["img"] * 255,
            )
        elif process_type == ProcessType.Verify:
            find_result = brushface.find_from_faces([face], db_path, skip_update=True)

            if len(find_result) == 0:
                logger.debug("No face matches.")
                return normal()

            first_match = find_result[0][1]

            user_id = Path(first_match["img_path"]).parent.name

            if user_id == current_user_id:
                logger.debug(f"Face matches, distance: {first_match["distance"]}.")
                cleanup()
                return void(lib.Message.Result.Success._instance())
        else:
            logger.error(f"Unknown process type {process_type}.")
            return void(lib.Message.Result.InternalError._instance())

        return normal()

    return send_frame


def handle_frame(_msg_type: str, ref: int):
    global current_user_id, processed_frame, busy

    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    frame_ref = libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame(ref)

    if not current_user_id or not process_type:
        logger.error("Received frame without handshake.")
        return lib.Message.Result.InternalError._instance()

    if busy:
        logger.error(f"Received frame with user ID {current_user_id} while busy.")
        return lib.Message.Register.Result.Next._instance()

    logger.debug(f"Processing frame with user ID {current_user_id}.")

    busy = True

    result = ctypes.pointer(lib.Message.Result.InternalError._instance())

    logger.debug("Trying to get frame content.")

    lib.byteArrayToPointer(
        lib.Message.Client.Frame.get_content(frame_ref),
        on_data(
            lib.Message.Client.Frame.get_format(frame_ref).decode(),
            lib.Message.Client.Frame.get_width(frame_ref),
            result,
        ),
    )

    logger.debug(f"Returning result.")

    return result.contents


def handle_handshake(_msg_type: str, ref: int):
    global current_user_id, process_type, start_time

    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    handshake_request = (
        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request(ref)
    )

    user_id = lib.Message.Handshake.Request.get_userId(handshake_request).decode()

    if current_user_id and current_user_id != user_id:
        logger.error(f"Received handshake while processing {current_user_id}.")
        return lib.Message.Handshake.Response.Failure._instance()

    current_user_id = user_id

    logger.trace(f"Database path is {db_path.resolve()}.")

    db_path.mkdir(parents=True, exist_ok=True)

    user_path = db_path / current_user_id

    if user_path.exists():  # TODO: Replace with a better check
        process_type = ProcessType.Verify
    else:
        process_type = ProcessType.Register
        user_path.mkdir()

    start_time = time()

    logger.info(
        f"Received handshake for {current_user_id}, process type is {process_type}."
    )

    return lib.Message.Handshake.Response.Success._instance()


def handle_cancel(_msg_type: str, _ref: int):
    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    logger.debug("Received cancel message, cleaning up.")

    cleanup()

    return lib.Message.Result.Cancelled._instance()
