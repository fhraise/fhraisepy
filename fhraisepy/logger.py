import ctypes

import fhraisepy
from fhraisepy.native.libfhraisepy import *


class Logger:
    __lib: xyz_xfqlittlefan_fhraise_py
    __logger: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger

    def __init__(self, tag: str, lib: xyz_xfqlittlefan_fhraise_py = None):
        if lib is None and fhraisepy.lib is None:
            raise ValueError("lib cannot be None.")

        self.__lib = lib or fhraisepy.lib
        self.__logger = self.__lib.Logger.Logger(ctypes.c_char_p(tag.encode()))

    def debug(self, message: str):
        self.__lib.Logger.debug(self.__logger, ctypes.c_char_p(message.encode()))

    def info(self, message: str):
        self.__lib.Logger.info(self.__logger, ctypes.c_char_p(message.encode()))

    def warn(self, message: str):
        self.__lib.Logger.warn(self.__logger, ctypes.c_char_p(message.encode()))

    def error(self, message: str):
        self.__lib.Logger.error(self.__logger, ctypes.c_char_p(message.encode()))

    def on_error(self, message):
        @ctypes.CFUNCTYPE(None, Throwable)
        def fun(throwable: Throwable):
            self.error(
                f"{message}: <{throwable.type.decode()}> {throwable.message.decode()}"
            )
            for i in range(throwable.stacktraceSize):
                self.error(throwable.stacktrace[i].decode())

        return fun
