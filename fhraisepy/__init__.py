"""
FhraisePy 是 Fhraise 项目的 Python 部分，主要负责 Fhraise 的机器学习部分。
"""

import ctypes

from fhraisepy.native.libfhraisepy import Throwable

throwable_ptr = ctypes.POINTER(Throwable)()
