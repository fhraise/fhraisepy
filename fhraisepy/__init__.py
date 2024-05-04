"""
FhraisePy 是 Fhraise 项目的 Python 部分，主要负责 Fhraise 的机器学习部分。
"""

import os
from pathlib import Path

import torch

os.environ["KERAS_BACKEND"] = "torch"

if bool(os.environ.get("FHRAISEPY_USE_CUDA", default="True")):
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
    env_file_path = Path("fhraisepy.env")

    if env_file_path.exists():
        with env_file_path.open() as env_file:
            for line in env_file:
                key, value = line.strip().split("=", maxsplit=1)
                os.environ[key] = value
            env_file.close()

    host = os.environ.get("FHRAISEPY_HOST", default=None)
    port = os.environ.get("FHRAISEPY_PORT", default=None)
    path = os.environ.get("FHRAISEPY_LIB_PATH", default=None)

    instant_run = os.environ.get("FHRAISEPY_INSTANT_RUN", default=False)

    if not instant_run and not (host and port and path):
        import sys

        argv = sys.argv[1:]

        if len(argv) == 1:
            path = argv[0]
        elif len(argv) == 2:
            host, port = argv
        elif len(argv) == 3:
            host, port, path = argv

    if not instant_run and not (host and port and path):
        host = host or input("Host (localhost): ")
        port = port or input("Port (11451): ")
        path = path or input("Path to library: ")

    host = host or "localhost"
    port = port or "11451"

    from fhraisepy.entrance import entrance

    entrance(host, int(port), path)
