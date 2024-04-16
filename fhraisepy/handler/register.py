from fhraisepy.native.libfhraisepy import *


def handle_register(
    lib: xyz_xfqlittlefan_fhraise_py, frame_ref_ptr: libfhraisepy_KNativePtr
):
    logger = lib.Logger.Logger(ctypes.c_char_p(__name__.encode()))

    frame_ref = libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Register_Frame(
        frame_ref_ptr.contents
    )

    call_id = lib.Message.Register.Frame.get_callId(frame_ref)
