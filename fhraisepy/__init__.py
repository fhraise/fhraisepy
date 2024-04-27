"""
FhraisePy 是 Fhraise 项目的 Python 部分，主要负责 Fhraise 的机器学习部分。
"""

import os

import torch

os.environ["KERAS_BACKEND"] = "torch"
torch.set_default_device("cuda")

from fhraisepy.native.libfhraisepy import *

lib: xyz_xfqlittlefan_fhraise_py
