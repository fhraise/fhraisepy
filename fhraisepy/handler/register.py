import ctypes
import inspect
from typing import Callable, Dict, Tuple

import brushface
import numpy as np
from brushface.models import YoloClient

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

    def success():
        global processed_frame
        processed_frame += 1

        return void(lib.Message.Register.Result.Success._instance())

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
            return void(lib.Message.Register.Result.LowResolution._instance())

        face = faces[0]

        confidence = face["face_area"]["confidence"]
        if confidence < confidence_threshold:
            logger.error(
                f"Face confidence is too low: {confidence}, threshold is {confidence_threshold}."
            )
            return void(lib.Message.Register.Result.LowResolution._instance())

        global current_call_id
        current_call_id = call_id

    return send_frame


def handle_register(frame_ref_ptr: int):
    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    frame_ref = libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Register_Frame(
        frame_ref_ptr
    )

    call_id = lib.Message.Register.Frame.get_callId(frame_ref).decode()

    if current_call_id is not None and current_call_id != call_id:
        logger.error(
            f"Received frame with call ID {call_id} while processing {current_call_id}."
        )
        return lib.Message.Register.Result.InternalError._instance()

    global busy

    if busy:
        logger.error(f"Received frame with call ID {call_id} while busy.")
        return lib.Message.Register.Result.InternalError._instance()

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
