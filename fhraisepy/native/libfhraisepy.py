"""
https://github.com/fhraise/Fhraise/commit/c99730361dbf4ffe4293f6bb9560ff6bc0fd37f7
"""

import ctypes

libfhraisepy_KBoolean = ctypes.c_bool
libfhraisepy_KChar = ctypes.c_ushort
libfhraisepy_KByte = ctypes.c_char
libfhraisepy_KShort = ctypes.c_short
libfhraisepy_KInt = ctypes.c_int
libfhraisepy_KLong = ctypes.c_longlong
libfhraisepy_KUByte = ctypes.c_ubyte
libfhraisepy_KUShort = ctypes.c_ushort
libfhraisepy_KUInt = ctypes.c_uint
libfhraisepy_KULong = ctypes.c_ulonglong
libfhraisepy_KFloat = ctypes.c_float
libfhraisepy_KDouble = ctypes.c_double
libfhraisepy_KNativePtr = ctypes.c_void_p


class Throwable(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_char_p),
        ("ref", libfhraisepy_KNativePtr),
        ("message", ctypes.c_char_p),
        ("stacktrace", ctypes.POINTER(ctypes.c_char_p)),
        ("stacktraceSize", ctypes.c_int),
    ]

    type: bytes
    ref: libfhraisepy_KNativePtr
    message: bytes
    stacktrace: ctypes.POINTER(ctypes.c_char_p)
    stacktraceSize: int


class libfhraisepy_KType(ctypes.Structure):
    _fields_ = []


class libfhraisepy_kref(ctypes.Structure):
    _fields_ = [("pinned", libfhraisepy_KNativePtr)]

    pinned: int


class libfhraisepy_kref_kotlin_Byte(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Short(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Int(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Long(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Float(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Double(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Char(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Boolean(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_Unit(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_UByte(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_UShort(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_UInt(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_ULong(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlin_ByteArray(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_kotlin_Any(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_serializer(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_kotlinx_serialization_descriptors_SerialDescriptor(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_kotlin_Array(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlinx_serialization_encoding_Decoder(libfhraisepy_kref):
    pass


class libfhraisepy_kref_kotlinx_serialization_encoding_Encoder(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_kotlinx_serialization_KSerializer(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_serializer(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response(
    libfhraisepy_kref
):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client(libfhraisepy_kref):
    pass


class libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger(libfhraisepy_kref):
    pass


class xyz_xfqlittlefan_fhraise_py(ctypes.Structure):
    class Message(ctypes.Structure):
        class Handshake(ctypes.Structure):
            class Request(ctypes.Structure):
                class serializer(ctypes.Structure):
                    _fields_ = [
                        (
                            "_type",
                            ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                        ),
                        (
                            "_instance",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_serializer
                            ),
                        ),
                        (
                            "get_descriptor",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlinx_serialization_descriptors_SerialDescriptor,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_serializer,
                            ),
                        ),
                        (
                            "childSerializers",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlin_Array,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_serializer,
                            ),
                        ),
                        (
                            "deserialize",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_serializer,
                                libfhraisepy_kref_kotlinx_serialization_encoding_Decoder,
                            ),
                        ),
                        (
                            "serialize",
                            ctypes.CFUNCTYPE(
                                None,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_serializer,
                                libfhraisepy_kref_kotlinx_serialization_encoding_Encoder,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                            ),
                        ),
                    ]

                _fields_ = [
                    ("$serializer", serializer),
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "Request",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                            ctypes.c_char_p,
                        ),
                    ),
                    (
                        "get_userId",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                        ),
                    ),
                    (
                        "component1",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                        ),
                    ),
                    (
                        "copy",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                            ctypes.c_char_p,
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                        ),
                    ),
                ]

                @staticmethod
                def get_userId(
                    thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request,
                ) -> bytes:
                    pass

            class Response(ctypes.Structure):
                class Success(ctypes.Structure):
                    _fields_ = [
                        (
                            "_type",
                            ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                        ),
                        (
                            "_instance",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success
                            ),
                        ),
                        (
                            "equals",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_KBoolean,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success,
                                libfhraisepy_kref_kotlin_Any,
                            ),
                        ),
                        (
                            "hashCode",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_KInt,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success,
                            ),
                        ),
                        (
                            "serializer",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlinx_serialization_KSerializer,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success,
                                libfhraisepy_kref_kotlin_Array,
                            ),
                        ),
                        (
                            "serializer_",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlinx_serialization_KSerializer,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success,
                            ),
                        ),
                        (
                            "toString",
                            ctypes.CFUNCTYPE(
                                ctypes.c_char_p,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success,
                            ),
                        ),
                    ]

                    @staticmethod
                    def _instance() -> (
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success
                    ):
                        pass

                class Failure(ctypes.Structure):
                    _fields_ = [
                        (
                            "_type",
                            ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                        ),
                        (
                            "_instance",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure
                            ),
                        ),
                        (
                            "equals",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_KBoolean,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure,
                                libfhraisepy_kref_kotlin_Any,
                            ),
                        ),
                        (
                            "hashCode",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_KInt,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure,
                            ),
                        ),
                        (
                            "serializer",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlinx_serialization_KSerializer,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure,
                                libfhraisepy_kref_kotlin_Array,
                            ),
                        ),
                        (
                            "serializer_",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlinx_serialization_KSerializer,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure,
                            ),
                        ),
                        (
                            "toString",
                            ctypes.CFUNCTYPE(
                                ctypes.c_char_p,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure,
                            ),
                        ),
                    ]

                    @staticmethod
                    def _instance() -> (
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure
                    ):
                        pass

                _fields_ = [
                    ("Success", Success),
                    ("Failure", Failure),
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "Response",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response,
                            libfhraisepy_KInt,
                            libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker,
                        ),
                    ),
                    (
                        "Response_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response
                        ),
                    ),
                ]

            _fields_ = [
                ("Request", Request),
                ("Response", Response),
                (
                    "_type",
                    ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                ),
                (
                    "Handshake",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake,
                        libfhraisepy_KInt,
                        libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker,
                    ),
                ),
                (
                    "Handshake_",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake
                    ),
                ),
            ]

        class Client(ctypes.Structure):
            class Frame(ctypes.Structure):
                class serializer(ctypes.Structure):
                    _fields_ = [
                        ("_type", ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType))),
                        (
                            "_instance",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_serializer
                            ),
                        ),
                        (
                            "get_descriptor",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlinx_serialization_descriptors_SerialDescriptor,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_serializer,
                            ),
                        ),
                        (
                            "childSerializers",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_kotlin_Array,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_serializer,
                            ),
                        ),
                        (
                            "deserialize",
                            ctypes.CFUNCTYPE(
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_serializer,
                                libfhraisepy_kref_kotlinx_serialization_encoding_Decoder,
                            ),
                        ),
                        (
                            "serialize",
                            ctypes.CFUNCTYPE(
                                None,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_serializer,
                                libfhraisepy_kref_kotlinx_serialization_encoding_Encoder,
                                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                            ),
                        ),
                    ]

                _fields_ = [
                    ("$serializer", serializer),
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "Frame",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                            ctypes.c_char_p,
                            libfhraisepy_KInt,
                            libfhraisepy_kref_kotlin_ByteArray,
                        ),
                    ),
                    (
                        "get_content",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlin_ByteArray,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                    (
                        "get_format",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                    (
                        "get_width",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                    (
                        "component1",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                    (
                        "component2",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                    (
                        "component3",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlin_ByteArray,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                    (
                        "copy",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                            ctypes.c_char_p,
                            libfhraisepy_KInt,
                            libfhraisepy_kref_kotlin_ByteArray,
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                        ),
                    ),
                ]

                @staticmethod
                def get_format(
                    thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                ) -> bytes:
                    pass

                @staticmethod
                def get_width(
                    thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                ) -> int:
                    pass

                @staticmethod
                def get_content(
                    thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame,
                ) -> libfhraisepy_kref_kotlin_ByteArray:
                    pass

            class Cancel(ctypes.Structure):
                _fields_ = [
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel
                ):
                    pass

            _fields_ = [
                ("Frame", Frame),
                ("Cancel", Cancel),
                (
                    "_type",
                    ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                ),
                (
                    "Client",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client,
                        libfhraisepy_KInt,
                        libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker,
                    ),
                ),
                (
                    "Client_",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client
                    ),
                ),
            ]

        class Result(ctypes.Structure):
            class Next(ctypes.Structure):
                _fields_ = [
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next
                ):
                    pass

            class Success(ctypes.Structure):
                _fields_ = [
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success
                ):
                    pass

            class NoFaces(ctypes.Structure):
                _fields_ = [
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces
                ):
                    pass

            class LowResolution(ctypes.Structure):
                _fields_ = [
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution
                ):
                    pass

            class InternalError(ctypes.Structure):
                _fields_ = [
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError
                ):
                    pass

            class Cancelled(ctypes.Structure):
                _fields_ = [
                    (
                        "_type",
                        ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                    ),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled
                ):
                    pass

            _fields_ = [
                ("Next", Next),
                ("Success", Success),
                ("NoFaces", NoFaces),
                ("LowResolution", LowResolution),
                ("InternalError", InternalError),
                ("Cancelled", Cancelled),
                (
                    "_type",
                    ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType)),
                ),
                (
                    "Result",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result,
                        libfhraisepy_KInt,
                        libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker,
                    ),
                ),
                (
                    "Result_",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result
                    ),
                ),
            ]

            @staticmethod
            def Result_() -> (
                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result
            ):
                pass

        class Ping(ctypes.Structure):
            class Request(ctypes.Structure):
                _fields_ = [
                    ("_type", ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType))),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request
                ):
                    pass

            class Response(ctypes.Structure):
                _fields_ = [
                    ("_type", ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType))),
                    (
                        "_instance",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response
                        ),
                    ),
                    (
                        "equals",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KBoolean,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response,
                            libfhraisepy_kref_kotlin_Any,
                        ),
                    ),
                    (
                        "hashCode",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_KInt,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response,
                        ),
                    ),
                    (
                        "serializer",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response,
                            libfhraisepy_kref_kotlin_Array,
                        ),
                    ),
                    (
                        "serializer_",
                        ctypes.CFUNCTYPE(
                            libfhraisepy_kref_kotlinx_serialization_KSerializer,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response,
                        ),
                    ),
                    (
                        "toString",
                        ctypes.CFUNCTYPE(
                            ctypes.c_char_p,
                            libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response,
                        ),
                    ),
                ]

                @staticmethod
                def _instance() -> (
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response
                ):
                    pass

            _fields_ = [
                ("Request", Request),
                ("Response", Response),
                ("_type", ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType))),
                (
                    "Ping",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping,
                        libfhraisepy_KInt,
                        libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker,
                    ),
                ),
                (
                    "Ping_",
                    ctypes.CFUNCTYPE(
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping
                    ),
                ),
            ]

        _fields_ = [
            ("Handshake", Handshake),
            ("Client", Client),
            ("Result", Result),
            ("Ping", Ping),
            ("_type", ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType))),
            (
                "Message",
                ctypes.CFUNCTYPE(
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message,
                    libfhraisepy_KInt,
                    libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker,
                ),
            ),
            (
                "Message_",
                ctypes.CFUNCTYPE(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message),
            ),
        ]

    class Client(ctypes.Structure):
        _fields_ = [
            ("_type", ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType))),
            (
                "Client",
                ctypes.CFUNCTYPE(
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client,
                    ctypes.c_char_p,
                    libfhraisepy_KUShort,
                ),
            ),
            (
                "connect",
                ctypes.CFUNCTYPE(
                    None,
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client,
                    ctypes.CFUNCTYPE(None),
                    ctypes.CFUNCTYPE(None, Throwable),
                    ctypes.CFUNCTYPE(None),
                ),
            ),
            (
                "receive",
                ctypes.CFUNCTYPE(
                    None,
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client,
                    ctypes.CFUNCTYPE(
                        libfhraisepy_KNativePtr,
                        ctypes.c_char_p,
                        libfhraisepy_KNativePtr,
                    ),
                ),
            ),
        ]

        @staticmethod
        def Client(
            host: ctypes.c_char_p, port: libfhraisepy_KUShort
        ) -> libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client:
            pass

        @staticmethod
        def connect(
            thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client,
            onConnect: ctypes.CFUNCTYPE(None),
            onError: ctypes.CFUNCTYPE(None, Throwable),
            onClose: ctypes.CFUNCTYPE(None),
        ):
            pass

        @staticmethod
        def receive(
            thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client,
            onMessage: ctypes.CFUNCTYPE(
                libfhraisepy_KNativePtr, ctypes.c_char_p, libfhraisepy_KNativePtr
            ),
            onError: ctypes.CFUNCTYPE(None, Throwable),
        ):
            pass

    class Logger(ctypes.Structure):
        _fields_ = [
            ("_type", ctypes.CFUNCTYPE(ctypes.POINTER(libfhraisepy_KType))),
            (
                "Logger",
                ctypes.CFUNCTYPE(
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
                    ctypes.c_char_p,
                ),
            ),
            (
                "debug",
                ctypes.CFUNCTYPE(
                    None,
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
                    ctypes.c_char_p,
                ),
            ),
            (
                "error",
                ctypes.CFUNCTYPE(
                    None,
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
                    ctypes.c_char_p,
                ),
            ),
            (
                "info",
                ctypes.CFUNCTYPE(
                    None,
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
                    ctypes.c_char_p,
                ),
            ),
            (
                "trace",
                ctypes.CFUNCTYPE(
                    None,
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
                    ctypes.c_char_p,
                ),
            ),
            (
                "warn",
                ctypes.CFUNCTYPE(
                    None,
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
                    ctypes.c_char_p,
                ),
            ),
        ]

        @staticmethod
        def Logger(
            tag: ctypes.c_char_p,
        ) -> libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger:
            pass

        @staticmethod
        def trace(
            thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
            message: ctypes.c_char_p,
        ):
            pass

        @staticmethod
        def debug(
            thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
            message: ctypes.c_char_p,
        ):
            pass

        @staticmethod
        def info(
            thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
            message: ctypes.c_char_p,
        ):
            pass

        @staticmethod
        def warn(
            thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
            message: ctypes.c_char_p,
        ):
            pass

        @staticmethod
        def error(
            thiz: libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger,
            message: ctypes.c_char_p,
        ):
            pass

    _fields_ = [
        ("Message", Message),
        ("Client", Client),
        ("Logger", Logger),
        (
            "byteArrayToPointer",
            ctypes.CFUNCTYPE(
                None,
                libfhraisepy_kref_kotlin_ByteArray,
                ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int),
            ),
        ),
    ]

    @staticmethod
    def byteArrayToPointer(
        byteArray: libfhraisepy_kref_kotlin_ByteArray,
        onData: ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int),
    ):
        pass


class _fhraise(ctypes.Structure):
    _fields_ = [("py", xyz_xfqlittlefan_fhraise_py)]

    py: xyz_xfqlittlefan_fhraise_py


class _xfqlittlefan(ctypes.Structure):
    _fields_ = [("fhraise", _fhraise)]

    fhraise: _fhraise


class _xyz(ctypes.Structure):
    _fields_ = [("xfqlittlefan", _xfqlittlefan)]

    xfqlittlefan: _xfqlittlefan


class _root(ctypes.Structure):
    _fields_ = [("xyz", _xyz)]

    xyz: _xyz


class _kotlin(ctypes.Structure):
    _fields_ = [("root", _root)]

    root: _root


class libfhraisepy_ExportedSymbols(ctypes.Structure):
    _fields_ = [
        ("DisposeStablePointer", ctypes.CFUNCTYPE(None, libfhraisepy_KNativePtr)),
        ("DisposeString", ctypes.CFUNCTYPE(None, ctypes.c_char_p)),
        (
            "IsInstance",
            ctypes.CFUNCTYPE(
                libfhraisepy_KBoolean,
                libfhraisepy_KNativePtr,
                ctypes.POINTER(libfhraisepy_KType),
            ),
        ),
        (
            "createNullableByte",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Byte, libfhraisepy_KByte),
        ),
        (
            "getNonNullValueOfByte",
            ctypes.CFUNCTYPE(libfhraisepy_KByte, libfhraisepy_kref_kotlin_Byte),
        ),
        (
            "createNullableShort",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Short, libfhraisepy_KShort),
        ),
        (
            "getNonNullValueOfShort",
            ctypes.CFUNCTYPE(libfhraisepy_KShort, libfhraisepy_kref_kotlin_Short),
        ),
        (
            "createNullableInt",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Int, libfhraisepy_KInt),
        ),
        (
            "getNonNullValueOfInt",
            ctypes.CFUNCTYPE(libfhraisepy_KInt, libfhraisepy_kref_kotlin_Int),
        ),
        (
            "createNullableLong",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Long, libfhraisepy_KLong),
        ),
        (
            "getNonNullValueOfLong",
            ctypes.CFUNCTYPE(libfhraisepy_KLong, libfhraisepy_kref_kotlin_Long),
        ),
        (
            "createNullableFloat",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Float, libfhraisepy_KFloat),
        ),
        (
            "getNonNullValueOfFloat",
            ctypes.CFUNCTYPE(libfhraisepy_KFloat, libfhraisepy_kref_kotlin_Float),
        ),
        (
            "createNullableDouble",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Double, libfhraisepy_KDouble),
        ),
        (
            "getNonNullValueOfDouble",
            ctypes.CFUNCTYPE(libfhraisepy_KDouble, libfhraisepy_kref_kotlin_Double),
        ),
        (
            "createNullableChar",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Char, libfhraisepy_KChar),
        ),
        (
            "getNonNullValueOfChar",
            ctypes.CFUNCTYPE(libfhraisepy_KChar, libfhraisepy_kref_kotlin_Char),
        ),
        (
            "createNullableBoolean",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Boolean, libfhraisepy_KBoolean),
        ),
        (
            "getNonNullValueOfBoolean",
            ctypes.CFUNCTYPE(libfhraisepy_KBoolean, libfhraisepy_kref_kotlin_Boolean),
        ),
        ("createNullableUnit", ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_Unit)),
        (
            "createNullableUByte",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_UByte, libfhraisepy_KUByte),
        ),
        (
            "getNonNullValueOfUByte",
            ctypes.CFUNCTYPE(libfhraisepy_KUByte, libfhraisepy_kref_kotlin_UByte),
        ),
        (
            "createNullableUShort",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_UShort, libfhraisepy_KUShort),
        ),
        (
            "getNonNullValueOfUShort",
            ctypes.CFUNCTYPE(libfhraisepy_KUShort, libfhraisepy_kref_kotlin_UShort),
        ),
        (
            "createNullableUInt",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_UInt, libfhraisepy_KUInt),
        ),
        (
            "getNonNullValueOfUInt",
            ctypes.CFUNCTYPE(libfhraisepy_KUInt, libfhraisepy_kref_kotlin_UInt),
        ),
        (
            "createNullableULong",
            ctypes.CFUNCTYPE(libfhraisepy_kref_kotlin_ULong, libfhraisepy_KULong),
        ),
        (
            "getNonNullValueOfULong",
            ctypes.CFUNCTYPE(libfhraisepy_KULong, libfhraisepy_kref_kotlin_ULong),
        ),
        ("kotlin", _kotlin),
    ]

    @staticmethod
    def DisposeStablePointer(ptr: libfhraisepy_KNativePtr):
        pass

    @staticmethod
    def DisposeString(string: ctypes.c_char_p):
        pass

    @staticmethod
    def IsInstance(
        ref: libfhraisepy_KNativePtr, ktype: ctypes.POINTER(libfhraisepy_KType)
    ) -> bool:
        pass

    kotlin: _kotlin
