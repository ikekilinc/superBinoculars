# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yuv.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yuv.proto',
  package='yuv',
  syntax='proto3',
  serialized_options=_b('\n\022edu.cmu.cs.gabrielB\tYUVProtos'),
  serialized_pb=_b('\n\tyuv.proto\x12\x03yuv\";\n\x08ToServer\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x10\n\x08rotation\x18\x03 \x01(\x05\x42\x1f\n\x12\x65\x64u.cmu.cs.gabrielB\tYUVProtosb\x06proto3')
)




_TOSERVER = _descriptor.Descriptor(
  name='ToServer',
  full_name='yuv.ToServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='yuv.ToServer.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='yuv.ToServer.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='yuv.ToServer.rotation', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['ToServer'] = _TOSERVER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToServer = _reflection.GeneratedProtocolMessageType('ToServer', (_message.Message,), {
  'DESCRIPTOR' : _TOSERVER,
  '__module__' : 'yuv_pb2'
  # @@protoc_insertion_point(class_scope:yuv.ToServer)
  })
_sym_db.RegisterMessage(ToServer)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)