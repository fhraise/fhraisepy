import ctypes

from fhraisepy.native.libfhraisepy import *


def handle_ping(lib: xyz_xfqlittlefan_fhraise_py, _: libfhraisepy_KNativePtr = None):
    return lib.Message.Ping.Response._instance()
