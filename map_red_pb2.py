# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: map_red.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='map_red.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmap_red.proto\"\x8f\x01\n\x15MastertoMapperRequest\x12\x16\n\x0enum_of_mappers\x18\x01 \x01(\x05\x12\x17\n\x0fnum_of_reducers\x18\x02 \x01(\x05\x12\x19\n\x11num_of_iterations\x18\x03 \x01(\x05\x12\x17\n\x0fnum_of_clusters\x18\x04 \x01(\x05\x12\x11\n\tfile_path\x18\x05 \x01(\t\";\n\x16MastertoMapperResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x11\n\tcentroids\x18\x02 \x03(\t\"\x90\x01\n\x16MastertoReducerRequest\x12\x16\n\x0enum_of_mappers\x18\x01 \x01(\x05\x12\x17\n\x0fnum_of_reducers\x18\x02 \x01(\x05\x12\x19\n\x11num_of_iterations\x18\x03 \x01(\x05\x12\x17\n\x0fnum_of_clusters\x18\x04 \x01(\x05\x12\x11\n\tcentroids\x18\x05 \x03(\t\"<\n\x17MastertoReducerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x11\n\tcentroids\x18\x02 \x03(\t\"\x89\x01\n\x16ReducertoMapperRequest\x12\x12\n\nreducer_id\x18\x01 \x01(\x05\x12\x16\n\x0enum_of_mappers\x18\x02 \x01(\x05\x12\x17\n\x0fnum_of_reducers\x18\x03 \x01(\x05\x12\x17\n\x0fnum_of_clusters\x18\x04 \x01(\x05\x12\x11\n\tfile_path\x18\x05 \x01(\t\"8\n\x17ReducertoMapperResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\r\n\x05\x66iles\x18\x02 \x03(\t2\xd7\x01\n\x06Kmeans\x12\x41\n\x0eMastertoMapper\x12\x16.MastertoMapperRequest\x1a\x17.MastertoMapperResponse\x12\x44\n\x0fMastertoReducer\x12\x17.MastertoReducerRequest\x1a\x18.MastertoReducerResponse\x12\x44\n\x0fReducertoMapper\x12\x17.ReducertoMapperRequest\x1a\x18.ReducertoMapperResponseb\x06proto3'
)




_MASTERTOMAPPERREQUEST = _descriptor.Descriptor(
  name='MastertoMapperRequest',
  full_name='MastertoMapperRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_of_mappers', full_name='MastertoMapperRequest.num_of_mappers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_reducers', full_name='MastertoMapperRequest.num_of_reducers', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_iterations', full_name='MastertoMapperRequest.num_of_iterations', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_clusters', full_name='MastertoMapperRequest.num_of_clusters', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='MastertoMapperRequest.file_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=161,
)


_MASTERTOMAPPERRESPONSE = _descriptor.Descriptor(
  name='MastertoMapperResponse',
  full_name='MastertoMapperResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='MastertoMapperResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='centroids', full_name='MastertoMapperResponse.centroids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=163,
  serialized_end=222,
)


_MASTERTOREDUCERREQUEST = _descriptor.Descriptor(
  name='MastertoReducerRequest',
  full_name='MastertoReducerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_of_mappers', full_name='MastertoReducerRequest.num_of_mappers', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_reducers', full_name='MastertoReducerRequest.num_of_reducers', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_iterations', full_name='MastertoReducerRequest.num_of_iterations', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_clusters', full_name='MastertoReducerRequest.num_of_clusters', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='centroids', full_name='MastertoReducerRequest.centroids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=225,
  serialized_end=369,
)


_MASTERTOREDUCERRESPONSE = _descriptor.Descriptor(
  name='MastertoReducerResponse',
  full_name='MastertoReducerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='MastertoReducerResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='centroids', full_name='MastertoReducerResponse.centroids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=371,
  serialized_end=431,
)


_REDUCERTOMAPPERREQUEST = _descriptor.Descriptor(
  name='ReducertoMapperRequest',
  full_name='ReducertoMapperRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reducer_id', full_name='ReducertoMapperRequest.reducer_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_mappers', full_name='ReducertoMapperRequest.num_of_mappers', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_reducers', full_name='ReducertoMapperRequest.num_of_reducers', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_of_clusters', full_name='ReducertoMapperRequest.num_of_clusters', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='ReducertoMapperRequest.file_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=434,
  serialized_end=571,
)


_REDUCERTOMAPPERRESPONSE = _descriptor.Descriptor(
  name='ReducertoMapperResponse',
  full_name='ReducertoMapperResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ReducertoMapperResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='files', full_name='ReducertoMapperResponse.files', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=573,
  serialized_end=629,
)

DESCRIPTOR.message_types_by_name['MastertoMapperRequest'] = _MASTERTOMAPPERREQUEST
DESCRIPTOR.message_types_by_name['MastertoMapperResponse'] = _MASTERTOMAPPERRESPONSE
DESCRIPTOR.message_types_by_name['MastertoReducerRequest'] = _MASTERTOREDUCERREQUEST
DESCRIPTOR.message_types_by_name['MastertoReducerResponse'] = _MASTERTOREDUCERRESPONSE
DESCRIPTOR.message_types_by_name['ReducertoMapperRequest'] = _REDUCERTOMAPPERREQUEST
DESCRIPTOR.message_types_by_name['ReducertoMapperResponse'] = _REDUCERTOMAPPERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MastertoMapperRequest = _reflection.GeneratedProtocolMessageType('MastertoMapperRequest', (_message.Message,), {
  'DESCRIPTOR' : _MASTERTOMAPPERREQUEST,
  '__module__' : 'map_red_pb2'
  # @@protoc_insertion_point(class_scope:MastertoMapperRequest)
  })
_sym_db.RegisterMessage(MastertoMapperRequest)

MastertoMapperResponse = _reflection.GeneratedProtocolMessageType('MastertoMapperResponse', (_message.Message,), {
  'DESCRIPTOR' : _MASTERTOMAPPERRESPONSE,
  '__module__' : 'map_red_pb2'
  # @@protoc_insertion_point(class_scope:MastertoMapperResponse)
  })
_sym_db.RegisterMessage(MastertoMapperResponse)

MastertoReducerRequest = _reflection.GeneratedProtocolMessageType('MastertoReducerRequest', (_message.Message,), {
  'DESCRIPTOR' : _MASTERTOREDUCERREQUEST,
  '__module__' : 'map_red_pb2'
  # @@protoc_insertion_point(class_scope:MastertoReducerRequest)
  })
_sym_db.RegisterMessage(MastertoReducerRequest)

MastertoReducerResponse = _reflection.GeneratedProtocolMessageType('MastertoReducerResponse', (_message.Message,), {
  'DESCRIPTOR' : _MASTERTOREDUCERRESPONSE,
  '__module__' : 'map_red_pb2'
  # @@protoc_insertion_point(class_scope:MastertoReducerResponse)
  })
_sym_db.RegisterMessage(MastertoReducerResponse)

ReducertoMapperRequest = _reflection.GeneratedProtocolMessageType('ReducertoMapperRequest', (_message.Message,), {
  'DESCRIPTOR' : _REDUCERTOMAPPERREQUEST,
  '__module__' : 'map_red_pb2'
  # @@protoc_insertion_point(class_scope:ReducertoMapperRequest)
  })
_sym_db.RegisterMessage(ReducertoMapperRequest)

ReducertoMapperResponse = _reflection.GeneratedProtocolMessageType('ReducertoMapperResponse', (_message.Message,), {
  'DESCRIPTOR' : _REDUCERTOMAPPERRESPONSE,
  '__module__' : 'map_red_pb2'
  # @@protoc_insertion_point(class_scope:ReducertoMapperResponse)
  })
_sym_db.RegisterMessage(ReducertoMapperResponse)



_KMEANS = _descriptor.ServiceDescriptor(
  name='Kmeans',
  full_name='Kmeans',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=632,
  serialized_end=847,
  methods=[
  _descriptor.MethodDescriptor(
    name='MastertoMapper',
    full_name='Kmeans.MastertoMapper',
    index=0,
    containing_service=None,
    input_type=_MASTERTOMAPPERREQUEST,
    output_type=_MASTERTOMAPPERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MastertoReducer',
    full_name='Kmeans.MastertoReducer',
    index=1,
    containing_service=None,
    input_type=_MASTERTOREDUCERREQUEST,
    output_type=_MASTERTOREDUCERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReducertoMapper',
    full_name='Kmeans.ReducertoMapper',
    index=2,
    containing_service=None,
    input_type=_REDUCERTOMAPPERREQUEST,
    output_type=_REDUCERTOMAPPERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KMEANS)

DESCRIPTOR.services_by_name['Kmeans'] = _KMEANS

# @@protoc_insertion_point(module_scope)