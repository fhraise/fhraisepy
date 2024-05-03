import inspect
from typing import Callable, Optional

import fhraisepy
from fhraisepy.handler.process import handle_cancel, handle_frame, handle_handshake
from fhraisepy.logger import Logger
from fhraisepy.native.libfhraisepy import *

lib = fhraisepy.lib

handlers = {
    "Handshake": {
        "Request": handle_handshake,
    },
    "Client": {
        "Frame": handle_frame,
        "Cancel": handle_cancel,
    },
    "Ping": {
        "Request": lambda a, b: lib.Message.Ping.Response._instance(),
    },
}


def find_handler(
    msg_type: str,
) -> Optional[Callable[[str, int], libfhraisepy_kref | None]]:
    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    logger.trace(f"Finding handler for message type {msg_type}")

    # xyz.xfqlittlefan.fhraise.py.Message.*
    split = msg_type.split(".")[5:]

    logger.trace(f"Split: {split}")

    current = split[0]
    handler = handlers

    while current in handler:
        logger.trace(f"Finding handler for {current} in {handler}")

        handler = handler[current]

        logger.trace(f"Found candidate: {handler}")

        if isinstance(handler, Callable):
            logger.trace(f"Found handler: {handler}")
            return handler

        if len(split) == 1:
            logger.debug(f"Handler for message type {msg_type} not found.")
            break

        split.pop(0)
        current = split[0]

    return None


@ctypes.CFUNCTYPE(libfhraisepy_KNativePtr, ctypes.c_char_p, libfhraisepy_KNativePtr)
def handle_message(
    raw_msg_type: bytes,
    ref: int,
):
    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    msg_type = raw_msg_type.decode()

    logger.debug(f"Received message: {msg_type}")

    handler = find_handler(msg_type)

    if not handler:
        logger.error(f"Handler for message type {msg_type} not found.")
        return lib.Message.Result.InternalError._instance()

    result = handler(msg_type, ref) or lib.Message.Result.InternalError._instance()

    logger.debug(f"Result: {result}")

    return result.pinned


def receive_message(
    client: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client,
):
    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    while True:
        logger.debug("Waiting for message...")

        lib.Client.receive(
            client,
            handle_message,
            logger.on_error("Failed to handle message"),
        )
