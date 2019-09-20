# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='egt.registration.v2',
  syntax='proto3',
  serialized_options=_b('\n)com.egt.client.registration.api.v2.commonP\001ZIgitlab.egt-ua.loc/apis/gen/user-management/registration-service/v2/common'),
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x13\x65gt.registration.v2\"K\n\x0c\x43ommonFields\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x12\n\npromo_code\x18\x02 \x01(\t\x12\x17\n\x0f\x61\x66\x66iliate_token\x18\x03 \x01(\t*A\n\x06Gender\x12\r\n\tNOT_KNOWN\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x12\x12\n\x0eNOT_APPLICABLE\x10\x03*I\n\x0cIdentityType\x12\x1d\n\x19IDENTITY_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rPERSONAL_CODE\x10\x01\x12\x07\n\x03\x43NP\x10\x02*u\n\x12RegistrationSource\x12\x16\n\x12SOURCE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x12\t\n\x05\x45MAIL\x10\x02\x12\t\n\x05PHONE\x10\x03\x12\x0c\n\x08\x46\x41\x43\x45\x42OOK\x10\x04\x12\r\n\tINSTAGRAM\x10\x05\x12\n\n\x06GOOGLE\x10\x06\x42x\n)com.egt.client.registration.api.v2.commonP\x01ZIgitlab.egt-ua.loc/apis/gen/user-management/registration-service/v2/commonb\x06proto3')
)

_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='egt.registration.v2.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_KNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_APPLICABLE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=114,
  serialized_end=179,
)
_sym_db.RegisterEnumDescriptor(_GENDER)

Gender = enum_type_wrapper.EnumTypeWrapper(_GENDER)
_IDENTITYTYPE = _descriptor.EnumDescriptor(
  name='IdentityType',
  full_name='egt.registration.v2.IdentityType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDENTITY_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSONAL_CODE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CNP', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=181,
  serialized_end=254,
)
_sym_db.RegisterEnumDescriptor(_IDENTITYTYPE)

IdentityType = enum_type_wrapper.EnumTypeWrapper(_IDENTITYTYPE)
_REGISTRATIONSOURCE = _descriptor.EnumDescriptor(
  name='RegistrationSource',
  full_name='egt.registration.v2.RegistrationSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SOURCE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACEBOOK', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTAGRAM', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=256,
  serialized_end=373,
)
_sym_db.RegisterEnumDescriptor(_REGISTRATIONSOURCE)

RegistrationSource = enum_type_wrapper.EnumTypeWrapper(_REGISTRATIONSOURCE)
NOT_KNOWN = 0
MALE = 1
FEMALE = 2
NOT_APPLICABLE = 3
IDENTITY_TYPE_UNSPECIFIED = 0
PERSONAL_CODE = 1
CNP = 2
SOURCE_UNSPECIFIED = 0
FULL = 1
EMAIL = 2
PHONE = 3
FACEBOOK = 4
INSTAGRAM = 5
GOOGLE = 6



_COMMONFIELDS = _descriptor.Descriptor(
  name='CommonFields',
  full_name='egt.registration.v2.CommonFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='locale', full_name='egt.registration.v2.CommonFields.locale', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='promo_code', full_name='egt.registration.v2.CommonFields.promo_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='affiliate_token', full_name='egt.registration.v2.CommonFields.affiliate_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=37,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['CommonFields'] = _COMMONFIELDS
DESCRIPTOR.enum_types_by_name['Gender'] = _GENDER
DESCRIPTOR.enum_types_by_name['IdentityType'] = _IDENTITYTYPE
DESCRIPTOR.enum_types_by_name['RegistrationSource'] = _REGISTRATIONSOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonFields = _reflection.GeneratedProtocolMessageType('CommonFields', (_message.Message,), {
  'DESCRIPTOR' : _COMMONFIELDS,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:egt.registration.v2.CommonFields)
  })
_sym_db.RegisterMessage(CommonFields)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
