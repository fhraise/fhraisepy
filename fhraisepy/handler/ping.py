import ctypes

from fhraisepy import lib
from fhraisepy.native.libfhraisepy import *


def handle_ping(_: int = None):
    return lib.Message.Ping.Response._instance()
