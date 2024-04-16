from fhraisepy import throwable_ptr
from fhraisepy.handler import handle_message
from fhraisepy.native.libfhraisepy import *


def entrance(lib_path: str, host: str, port: int):
    cdll = ctypes.CDLL(lib_path)

    cdll.libfhraisepy_symbols.argtypes = ()
    cdll.libfhraisepy_symbols.restype = ctypes.POINTER(libfhraisepy_ExportedSymbols)

    lib: xyz_xfqlittlefan_fhraise_py = (
        cdll.libfhraisepy_symbols().contents.kotlin.root.xyz.xfqlittlefan.fhraise.py
    )

    logger = lib.Logger.Logger(ctypes.c_char_p(__name__.encode()))

    client = lib.Client.Client(
        ctypes.c_char_p(host.encode()), libfhraisepy_KUShort(port)
    )

    connection_result = lib.Client.connect(client, ctypes.pointer(throwable_ptr))

    if not connection_result:
        lib.Logger.error(
            logger,
            ctypes.c_char_p(
                f"Connection failed: {throwable_ptr.contents.message}".encode()
            ),
        )
        return

    lib.Logger.debug(logger, ctypes.c_char_p("Connection established.".encode()))

    handle_message(lib, client)
