import sys

import fhraisepy
from fhraisepy.native.libfhraisepy import *


def entrance(lib_path: str, host: str, port: int):
    cdll = ctypes.CDLL(lib_path)

    cdll.libfhraisepy_symbols.argtypes = ()
    cdll.libfhraisepy_symbols.restype = ctypes.POINTER(libfhraisepy_ExportedSymbols)

    fhraisepy.lib = (
        cdll.libfhraisepy_symbols().contents.kotlin.root.xyz.xfqlittlefan.fhraise.py
    )

    lib = fhraisepy.lib

    from fhraisepy.logger import Logger

    logger = Logger(__name__)

    client = lib.Client.Client(
        ctypes.c_char_p(host.encode()), libfhraisepy_KUShort(port)
    )

    @ctypes.CFUNCTYPE(None)
    def on_close():
        logger.info("Connection closed.")
        sys.exit(0)

    success = lib.Client.connect(client, logger.on_error("Connection failed"), on_close)

    if not success:
        return

    logger.info("Connection established.")

    from fhraisepy.handler import receive_message

    receive_message(client)
