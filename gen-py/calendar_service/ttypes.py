#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class RankType:
  NUB = 1
  OBERNUB = 2
  BOSS = 3

  _VALUES_TO_NAMES = {
    1: "NUB",
    2: "OBERNUB",
    3: "BOSS",
  }

  _NAMES_TO_VALUES = {
    "NUB": 1,
    "OBERNUB": 2,
    "BOSS": 3,
  }


class User:
  """
  Attributes:
   - uid
   - firstname
   - middlename
   - lastname
   - phone
   - rank
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'uid', None, None, ), # 1
    (2, TType.STRING, 'firstname', None, None, ), # 2
    (3, TType.STRING, 'middlename', None, None, ), # 3
    (4, TType.STRING, 'lastname', None, None, ), # 4
    (5, TType.STRING, 'phone', None, None, ), # 5
    (6, TType.I32, 'rank', None, None, ), # 6
  )

  def __init__(self, uid=None, firstname=None, middlename=None, lastname=None, phone=None, rank=None,):
    self.uid = uid
    self.firstname = firstname
    self.middlename = middlename
    self.lastname = lastname
    self.phone = phone
    self.rank = rank

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.uid = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.firstname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.middlename = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.lastname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.phone = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.rank = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('User')
    if self.uid is not None:
      oprot.writeFieldBegin('uid', TType.I32, 1)
      oprot.writeI32(self.uid)
      oprot.writeFieldEnd()
    if self.firstname is not None:
      oprot.writeFieldBegin('firstname', TType.STRING, 2)
      oprot.writeString(self.firstname)
      oprot.writeFieldEnd()
    if self.middlename is not None:
      oprot.writeFieldBegin('middlename', TType.STRING, 3)
      oprot.writeString(self.middlename)
      oprot.writeFieldEnd()
    if self.lastname is not None:
      oprot.writeFieldBegin('lastname', TType.STRING, 4)
      oprot.writeString(self.lastname)
      oprot.writeFieldEnd()
    if self.phone is not None:
      oprot.writeFieldBegin('phone', TType.STRING, 5)
      oprot.writeString(self.phone)
      oprot.writeFieldEnd()
    if self.rank is not None:
      oprot.writeFieldBegin('rank', TType.I32, 6)
      oprot.writeI32(self.rank)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class InvalidValueException(TException):
  """
  Attributes:
   - error_code
   - error_msg
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'error_code', None, None, ), # 1
    (2, TType.STRING, 'error_msg', None, None, ), # 2
  )

  def __init__(self, error_code=None, error_msg=None,):
    self.error_code = error_code
    self.error_msg = error_msg

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.error_code = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.error_msg = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('InvalidValueException')
    if self.error_code is not None:
      oprot.writeFieldBegin('error_code', TType.I32, 1)
      oprot.writeI32(self.error_code)
      oprot.writeFieldEnd()
    if self.error_msg is not None:
      oprot.writeFieldBegin('error_msg', TType.STRING, 2)
      oprot.writeString(self.error_msg)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
