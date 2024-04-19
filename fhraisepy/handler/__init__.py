import inspect

import fhraisepy
from fhraisepy.handler.ping import handle_ping
from fhraisepy.handler.register import handle_register
from fhraisepy.logger import Logger
from fhraisepy.native.libfhraisepy import *

lib = fhraisepy.lib

handlers = {
    "xyz.xfqlittlefan.fhraise.py.Message.Ping.Request": handle_ping,
    "xyz.xfqlittlefan.fhraise.py.Message.Register.Frame": handle_register,
}


@ctypes.CFUNCTYPE(libfhraisepy_KNativePtr, ctypes.c_char_p, libfhraisepy_KNativePtr)
def handle_message(
    raw_msg_type: bytes,
    msg_ref: int,
):
    logger = Logger(f"{__name__}:{inspect.currentframe().f_code.co_name}")

    msg_type = raw_msg_type.decode()

    logger.debug(f"Received message: {msg_type}")

    result: libfhraisepy_kref | None

    if msg_type in handlers:
        result = handlers[msg_type](lib, msg_ref)
    else:
        logger.error(f"Handler for message type {msg_type} not found.")
        result = None

    logger.debug(f"Result: {result}")

    return result.pinned if result else None


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
