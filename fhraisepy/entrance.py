import fhraisepy
from fhraisepy.native.libfhraisepy import *


def entrance(host: str, port: int, lib_path: str = None):
    if lib_path:
        fhraisepy.load_lib(lib_path)

    lib = fhraisepy.lib

    from fhraisepy.logger import Logger

    logger = Logger(__name__)

    client = lib.Client.Client(
        ctypes.c_char_p(host.encode()), libfhraisepy_KUShort(port)
    )

    @ctypes.CFUNCTYPE(None)
    def on_connect():
        logger.info("Connection established.")

        from fhraisepy.handler import receive_message

        receive_message(client)

    @ctypes.CFUNCTYPE(None)
    def on_close():
        logger.info("Connection closed.")

    lib.Client.connect(
        client, on_connect, logger.on_error("Connection failed"), on_close
    )
