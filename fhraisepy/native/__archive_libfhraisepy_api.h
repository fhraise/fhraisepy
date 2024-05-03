// https://github.com/fhraise/Fhraise/commit/75fc033643f06985c782610023abb0c4e511d462

#ifndef KONAN_LIBFHRAISEPY_H
#define KONAN_LIBFHRAISEPY_H
#ifdef __cplusplus
extern "C" {
#endif
#ifdef __cplusplus
typedef bool            libfhraisepy_KBoolean;
#else
typedef _Bool           libfhraisepy_KBoolean;
#endif
typedef unsigned short     libfhraisepy_KChar;
typedef signed char        libfhraisepy_KByte;
typedef short              libfhraisepy_KShort;
typedef int                libfhraisepy_KInt;
typedef long long          libfhraisepy_KLong;
typedef unsigned char      libfhraisepy_KUByte;
typedef unsigned short     libfhraisepy_KUShort;
typedef unsigned int       libfhraisepy_KUInt;
typedef unsigned long long libfhraisepy_KULong;
typedef float              libfhraisepy_KFloat;
typedef double             libfhraisepy_KDouble;
#ifndef _MSC_VER
typedef float __attribute__ ((__vector_size__ (16))) libfhraisepy_KVector128;
#else
#include <xmmintrin.h>
typedef __m128 libfhraisepy_KVector128;
#endif
typedef void*              libfhraisepy_KNativePtr;
struct libfhraisepy_KType;
typedef struct libfhraisepy_KType libfhraisepy_KType;

typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Byte;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Short;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Int;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Long;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Float;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Double;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Char;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Boolean;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Unit;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_UByte;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_UShort;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_UInt;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_ULong;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_ByteArray;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Any;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_$serializer;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlinx_serialization_descriptors_SerialDescriptor;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlin_Array;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlinx_serialization_encoding_Decoder;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlinx_serialization_encoding_Encoder;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_kotlinx_serialization_KSerializer;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_FrameFormat;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_FrameFormat_Rgb;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_$serializer;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client;
typedef struct {
  libfhraisepy_KNativePtr pinned;
} libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger;


typedef struct {
  /* Service functions. */
  void (*DisposeStablePointer)(libfhraisepy_KNativePtr ptr);
  void (*DisposeString)(const char* string);
  libfhraisepy_KBoolean (*IsInstance)(libfhraisepy_KNativePtr ref, const libfhraisepy_KType* type);
  libfhraisepy_kref_kotlin_Byte (*createNullableByte)(libfhraisepy_KByte);
  libfhraisepy_KByte (*getNonNullValueOfByte)(libfhraisepy_kref_kotlin_Byte);
  libfhraisepy_kref_kotlin_Short (*createNullableShort)(libfhraisepy_KShort);
  libfhraisepy_KShort (*getNonNullValueOfShort)(libfhraisepy_kref_kotlin_Short);
  libfhraisepy_kref_kotlin_Int (*createNullableInt)(libfhraisepy_KInt);
  libfhraisepy_KInt (*getNonNullValueOfInt)(libfhraisepy_kref_kotlin_Int);
  libfhraisepy_kref_kotlin_Long (*createNullableLong)(libfhraisepy_KLong);
  libfhraisepy_KLong (*getNonNullValueOfLong)(libfhraisepy_kref_kotlin_Long);
  libfhraisepy_kref_kotlin_Float (*createNullableFloat)(libfhraisepy_KFloat);
  libfhraisepy_KFloat (*getNonNullValueOfFloat)(libfhraisepy_kref_kotlin_Float);
  libfhraisepy_kref_kotlin_Double (*createNullableDouble)(libfhraisepy_KDouble);
  libfhraisepy_KDouble (*getNonNullValueOfDouble)(libfhraisepy_kref_kotlin_Double);
  libfhraisepy_kref_kotlin_Char (*createNullableChar)(libfhraisepy_KChar);
  libfhraisepy_KChar (*getNonNullValueOfChar)(libfhraisepy_kref_kotlin_Char);
  libfhraisepy_kref_kotlin_Boolean (*createNullableBoolean)(libfhraisepy_KBoolean);
  libfhraisepy_KBoolean (*getNonNullValueOfBoolean)(libfhraisepy_kref_kotlin_Boolean);
  libfhraisepy_kref_kotlin_Unit (*createNullableUnit)(void);
  libfhraisepy_kref_kotlin_UByte (*createNullableUByte)(libfhraisepy_KUByte);
  libfhraisepy_KUByte (*getNonNullValueOfUByte)(libfhraisepy_kref_kotlin_UByte);
  libfhraisepy_kref_kotlin_UShort (*createNullableUShort)(libfhraisepy_KUShort);
  libfhraisepy_KUShort (*getNonNullValueOfUShort)(libfhraisepy_kref_kotlin_UShort);
  libfhraisepy_kref_kotlin_UInt (*createNullableUInt)(libfhraisepy_KUInt);
  libfhraisepy_KUInt (*getNonNullValueOfUInt)(libfhraisepy_kref_kotlin_UInt);
  libfhraisepy_kref_kotlin_ULong (*createNullableULong)(libfhraisepy_KULong);
  libfhraisepy_KULong (*getNonNullValueOfULong)(libfhraisepy_kref_kotlin_ULong);

  /* User functions. */
  struct {
    struct {
      struct {
        struct {
          struct {
            struct {
              struct {
                struct {
                  struct {
                    struct {
                      libfhraisepy_KType* (*_type)(void);
                      libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_$serializer (*_instance)();
                      libfhraisepy_kref_kotlinx_serialization_descriptors_SerialDescriptor (*get_descriptor)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_$serializer thiz);
                      libfhraisepy_kref_kotlin_Array (*childSerializers)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_$serializer thiz);
                      libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request (*deserialize)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_$serializer thiz, libfhraisepy_kref_kotlinx_serialization_encoding_Decoder decoder);
                      void (*serialize)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request_$serializer thiz, libfhraisepy_kref_kotlinx_serialization_encoding_Encoder encoder, libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request value);
                    } $serializer;
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request (*Request)(const char* userId);
                    const char* (*get_userId)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request thiz);
                    const char* (*component1)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request thiz);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request (*copy)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request thiz, const char* userId);
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Request thiz);
                  } Request;
                  struct {
                    struct {
                      libfhraisepy_KType* (*_type)(void);
                      libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success (*_instance)();
                      libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success thiz, libfhraisepy_kref_kotlin_Any other);
                      libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success thiz);
                      libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                      libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success thiz);
                      const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Success thiz);
                    } Success;
                    struct {
                      libfhraisepy_KType* (*_type)(void);
                      libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure (*_instance)();
                      libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure thiz, libfhraisepy_kref_kotlin_Any other);
                      libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure thiz);
                      libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                      libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure thiz);
                      const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response_Failure thiz);
                    } Failure;
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response (*Response)(libfhraisepy_KInt seen0, libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker serializationConstructorMarker);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake_Response (*Response_)();
                  } Response;
                  libfhraisepy_KType* (*_type)(void);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake (*Handshake)(libfhraisepy_KInt seen0, libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker serializationConstructorMarker);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Handshake (*Handshake_)();
                } Handshake;
                struct {
                  struct {
                    struct {
                      struct {
                        libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_FrameFormat (*get)(); /* enum entry for Rgb. */
                      } Rgb;
                      libfhraisepy_KType* (*_type)(void);
                    } FrameFormat;
                    struct {
                      libfhraisepy_KType* (*_type)(void);
                      libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_$serializer (*_instance)();
                      libfhraisepy_kref_kotlinx_serialization_descriptors_SerialDescriptor (*get_descriptor)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_$serializer thiz);
                      libfhraisepy_kref_kotlin_Array (*childSerializers)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_$serializer thiz);
                      libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame (*deserialize)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_$serializer thiz, libfhraisepy_kref_kotlinx_serialization_encoding_Decoder decoder);
                      void (*serialize)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_$serializer thiz, libfhraisepy_kref_kotlinx_serialization_encoding_Encoder encoder, libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame value);
                    } $serializer;
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame (*Frame)(const char* userId, libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_FrameFormat format, libfhraisepy_KInt width, libfhraisepy_kref_kotlin_ByteArray content);
                    libfhraisepy_kref_kotlin_ByteArray (*get_content)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_FrameFormat (*get_format)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    const char* (*get_userId)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    libfhraisepy_KInt (*get_width)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    const char* (*component1)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_FrameFormat (*component2)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    libfhraisepy_KInt (*component3)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    libfhraisepy_kref_kotlin_ByteArray (*component4)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame (*copy)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz, const char* userId, libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame_FrameFormat format, libfhraisepy_KInt width, libfhraisepy_kref_kotlin_ByteArray content);
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Frame thiz);
                  } Frame;
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client_Cancel thiz);
                  } Cancel;
                  libfhraisepy_KType* (*_type)(void);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client (*Client)(libfhraisepy_KInt seen0, libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker serializationConstructorMarker);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Client (*Client_)();
                } Client;
                struct {
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Next thiz);
                  } Next;
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Success thiz);
                  } Success;
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_NoFaces thiz);
                  } NoFaces;
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_LowResolution thiz);
                  } LowResolution;
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_InternalError thiz);
                  } InternalError;
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result_Cancelled thiz);
                  } Cancelled;
                  libfhraisepy_KType* (*_type)(void);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result (*Result)(libfhraisepy_KInt seen0, libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker serializationConstructorMarker);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Result (*Result_)();
                } Result;
                struct {
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Request thiz);
                  } Request;
                  struct {
                    libfhraisepy_KType* (*_type)(void);
                    libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response (*_instance)();
                    libfhraisepy_KBoolean (*equals)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response thiz, libfhraisepy_kref_kotlin_Any other);
                    libfhraisepy_KInt (*hashCode)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response thiz);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response thiz, libfhraisepy_kref_kotlin_Array typeParamsSerializers);
                    libfhraisepy_kref_kotlinx_serialization_KSerializer (*serializer_)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response thiz);
                    const char* (*toString)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping_Response thiz);
                  } Response;
                  libfhraisepy_KType* (*_type)(void);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping (*Ping)(libfhraisepy_KInt seen0, libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker serializationConstructorMarker);
                  libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message_Ping (*Ping_)();
                } Ping;
                libfhraisepy_KType* (*_type)(void);
                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message (*Message)(libfhraisepy_KInt seen0, libfhraisepy_kref_kotlinx_serialization_internal_SerializationConstructorMarker serializationConstructorMarker);
                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Message (*Message_)();
              } Message;
              struct {
                libfhraisepy_KType* (*_type)(void);
                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client (*Client)(const char* host, libfhraisepy_KUShort port);
                libfhraisepy_KBoolean (*connect)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client thiz, void* onError, void* onClose);
                libfhraisepy_KBoolean (*receive)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Client thiz, void* onMessage, void* onError);
              } Client;
              struct {
                libfhraisepy_KType* (*_type)(void);
                libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger (*Logger)(const char* tag);
                void (*debug)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger thiz, const char* message);
                void (*error)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger thiz, const char* message);
                void (*info)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger thiz, const char* message);
                void (*trace)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger thiz, const char* message);
                void (*warn)(libfhraisepy_kref_xyz_xfqlittlefan_fhraise_py_Logger thiz, const char* message);
              } Logger;
              void (*byteArrayToPointer)(libfhraisepy_kref_kotlin_ByteArray byteArray, void* onData);
            } py;
          } fhraise;
        } xfqlittlefan;
      } xyz;
    } root;
  } kotlin;
} libfhraisepy_ExportedSymbols;
extern libfhraisepy_ExportedSymbols* libfhraisepy_symbols(void);
#ifdef __cplusplus
}  /* extern "C" */
#endif
#endif  /* KONAN_LIBFHRAISEPY_H */
