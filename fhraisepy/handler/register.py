import inspect
from pathlib import Path
from typing import Callable, Dict

import brushface
import cv2
import numpy as np

from fhraisepy import lib
from fhraisepy.logger import Logger
from fhraisepy.native.libfhraisepy import *

frame_converters: Dict[int, Callable[[np.ndarray, int], np.ndarray]] = {
    lib.Message.FrameFormat.Rgb.get().pinned: lambda frame, width: frame.reshape(
        (width, -1, 3)
    )
}
"""
将任意格式的帧转换为 RGB 3 维数组。
"""

db_path = Path("images")
confidence_threshold = 0.8
num_images = 5

current_call_id: str | None = None
processed_frame = 0
busy = False


def on_data(
    call_id: str,
    frame_format: int,
    width: int,
    result: ctypes.POINTER(libfhraisepy_kref),
):
    def void(ref: libfhraisepy_kref):
        global busy
        busy = False

        result.contents = ref

    def next():
        global processed_frame
        processed_frame += 1

        if processed_frame == num_images:
            global current_call_id
            current_call_id = None
            processed_frame = 0

            brushface.update_datastore(db_path)

            return void(lib.Message.Register.Result.Success._instance())

        return void(lib.Message.Register.Result.Next._instance())

    @ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_char), ctypes.c_int)
    def send_frame(data: ctypes.POINTER(ctypes.c_char), size: int):
        logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

        frame = np.array(data[:size])

        logger.debug(f"Received frame with size {size}.")

        if frame_format not in frame_converters:
            logger.error(f"Converter for frame format {frame_format} not found.")
            return void(lib.Message.Register.Result.InternalError._instance())

        converter = frame_converters[frame_format]

        logger.debug(f"Converter {converter.__name__} is used for this frame.")

        frame = converter(frame, width)
        faces = brushface.extract_faces(frame, enforce_detection=False)
        faces.sort(key=lambda x: x["face_area"]["confidence"], reverse=True)

        if len(faces) == 0:
            logger.error("No faces detected.")
            return void(lib.Message.Register.Result.NoFaces._instance())

        face = faces[0]

        confidence = face["face_area"]["confidence"]
        if confidence < confidence_threshold:
            logger.error(
                f"Face confidence is too low: {confidence}, threshold is {confidence_threshold}."
            )
            return void(lib.Message.Register.Result.LowResolution._instance())

        global current_call_id
        current_call_id = call_id

        cv2.imwrite(str(db_path / call_id / f"{processed_frame}.jpg"), face["img"])
        return next()

    return send_frame


def handle_register(frame_ref_ptr: int):
    global current_call_id, processed_frame, busy

    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    if frame_ref_ptr == lib.Message.Register.Cancel._instance().pinned:
        current_call_id = None
        processed_frame = 0
        busy = False
        return lib.Message.Register.Result.Cancelled._instance()

    frame_ref = libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Register_Frame(
        frame_ref_ptr
    )

    call_id = lib.Message.Register.Frame.get_callId(frame_ref).decode()

    if current_call_id is not None and current_call_id != call_id:
        logger.error(
            f"Received frame with call ID {call_id} while processing {current_call_id}."
        )
        return lib.Message.Register.Result.InternalError._instance()

    if busy:
        logger.error(f"Received frame with call ID {call_id} while busy.")
        return lib.Message.Register.Result.Next._instance()

    logger.debug(f"Processing frame with call ID {call_id}.")

    busy = True

    result = ctypes.pointer(lib.Message.Register.Result.Result_())

    lib.byteArrayToPointer(
        lib.Message.Register.Frame.get_content(frame_ref),
        on_data(
            call_id,
            lib.Message.Register.Frame.get_format(frame_ref).pinned,
            lib.Message.Register.Frame.get_width(frame_ref),
            result,
        ),
    )

    return result.contents
