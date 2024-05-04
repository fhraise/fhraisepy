"""
FhraisePy 是 Fhraise 项目的 Python 部分，主要负责 Fhraise 的机器学习部分。
"""

import os

import torch

os.environ["KERAS_BACKEND"] = "torch"
torch.set_default_device("cuda")

from fhraisepy.native.libfhraisepy import *

symbols: libfhraisepy_ExportedSymbols
lib: xyz_xfqlittlefan_fhraise_py


def load_lib(lib_path: str):
    cdll = ctypes.CDLL(lib_path)

    cdll.libfhraisepy_symbols.argtypes = ()
    cdll.libfhraisepy_symbols.restype = ctypes.POINTER(libfhraisepy_ExportedSymbols)

    global symbols, lib
    symbols = cdll.libfhraisepy_symbols().contents
    lib = symbols.kotlin.root.xyz.xfqlittlefan.fhraise.py

    return lib


if __name__ == "__main__":
    import sys

    sys.argv = sys.argv[1:]

    if len(sys.argv) == 3:
        host, port, path = sys.argv
    else:
        host = None
        port = None
        path = None

    from fhraisepy.entrance import entrance

    entrance(
        host or input("Host (localhost): ") or "localhost",
        int(port or input("Port (11451): ") or "11451"),
        path or input("Path to library: "),
    )
