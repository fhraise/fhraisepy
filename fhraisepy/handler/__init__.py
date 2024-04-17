import inspect

from fhraisepy import throwable_ptr
from fhraisepy.handler.ping import handle_ping
from fhraisepy.handler.register import handle_register
from fhraisepy.native.libfhraisepy import *

handlers = {
    b"xyz.xfqlittlefan.fhraise.py.Message.Ping.Request": handle_ping,
    b"xyz.xfqlittlefan.fhraise.py.Message.Register.Frame": handle_register,
}


def handle_message(
    lib: xyz_xfqlittlefan_fhraise_py,
    client: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client,
):
    logger = lib.Logger.Logger(
        ctypes.c_char_p(f"{__name__}:{inspect.currentframe().f_code.co_name}".encode())
    )

    while True:
        lib.Logger.debug(
            logger, ctypes.c_char_p("Preparing to receive message.".encode())
        )

        msg_type = ctypes.c_char_p()
        msg_ref = libfhraisepy_KNativePtr()

        lib.Logger.debug(logger, ctypes.c_char_p("Waiting for message...".encode()))

        receive_successful = lib.Client.receive(
            client,
            ctypes.pointer(msg_type),
            ctypes.pointer(msg_ref),
            ctypes.pointer(throwable_ptr),
            ctypes.CFUNCTYPE(libfhraisepy_KNativePtr)(
                get_result_fun(lib, msg_type, msg_ref)
            ),
        )

        if not receive_successful:
            lib.Logger.error(
                logger,
                ctypes.c_char_p(
                    f"Failed to receive message: {throwable_ptr.contents.message}".encode()
                ),
            )


def get_result_fun(
    lib: xyz_xfqlittlefan_fhraise_py,
    msg_type: ctypes.c_char_p,
    msg_ref: libfhraisepy_KNativePtr,
):
    logger = lib.Logger.Logger(
        ctypes.c_char_p(f"{__name__}:{inspect.currentframe().f_code.co_name}".encode())
    )

    def fun():
        lib.Logger.debug(
            logger, ctypes.c_char_p(f"Received message: {msg_type.value}".encode())
        )

        result: libfhraisepy_kref | None

        if msg_type.value in handlers:
            result = handlers[msg_type.value](lib, msg_ref)
        else:
            lib.Logger.error(
                logger,
                ctypes.c_char_p(
                    f"Handler for message type {msg_type.value} not found.".encode()
                ),
            )
            result = None

        lib.Logger.debug(logger, ctypes.c_char_p(f"Result: {result}".encode()))

        return result.pinned or None

    return fun
