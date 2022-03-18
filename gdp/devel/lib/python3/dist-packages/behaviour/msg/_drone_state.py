# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from behaviour/drone_state.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import behaviour.msg
import std_msgs.msg

class drone_state(genpy.Message):
  _md5sum = "5309d0e3c8a877ad2b981cbca29cefc4"
  _type = "behaviour/drone_state"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
int8 drone_id
int8 mode
int8 type
float64 messagetime
drone_geometry drone_geometry
int8 battery
int8 drone_soh
score score
task task
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: behaviour/drone_geometry
Header header
float64 lat
float64 lon
float32 alt
float32 yaw
float32 roll
float32 pitch
================================================================================
MSG: behaviour/score
Header header
int8 drone_id
int8 task_id
float32 score

================================================================================
MSG: behaviour/task
Header header
int8 task_id
task_geometry task_geometry
int8 allocated
int8 type

================================================================================
MSG: behaviour/task_geometry
Header header
float64 lat
float64 lon
float32 alt
"""
  __slots__ = ['header','drone_id','mode','type','messagetime','drone_geometry','battery','drone_soh','score','task']
  _slot_types = ['std_msgs/Header','int8','int8','int8','float64','behaviour/drone_geometry','int8','int8','behaviour/score','behaviour/task']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,drone_id,mode,type,messagetime,drone_geometry,battery,drone_soh,score,task

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(drone_state, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_id is None:
        self.drone_id = 0
      if self.mode is None:
        self.mode = 0
      if self.type is None:
        self.type = 0
      if self.messagetime is None:
        self.messagetime = 0.
      if self.drone_geometry is None:
        self.drone_geometry = behaviour.msg.drone_geometry()
      if self.battery is None:
        self.battery = 0
      if self.drone_soh is None:
        self.drone_soh = 0
      if self.score is None:
        self.score = behaviour.msg.score()
      if self.task is None:
        self.task = behaviour.msg.task()
    else:
      self.header = std_msgs.msg.Header()
      self.drone_id = 0
      self.mode = 0
      self.type = 0
      self.messagetime = 0.
      self.drone_geometry = behaviour.msg.drone_geometry()
      self.battery = 0
      self.drone_soh = 0
      self.score = behaviour.msg.score()
      self.task = behaviour.msg.task()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3bd3I().pack(_x.drone_id, _x.mode, _x.type, _x.messagetime, _x.drone_geometry.header.seq, _x.drone_geometry.header.stamp.secs, _x.drone_geometry.header.stamp.nsecs))
      _x = self.drone_geometry.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d4f2b3I().pack(_x.drone_geometry.lat, _x.drone_geometry.lon, _x.drone_geometry.alt, _x.drone_geometry.yaw, _x.drone_geometry.roll, _x.drone_geometry.pitch, _x.battery, _x.drone_soh, _x.score.header.seq, _x.score.header.stamp.secs, _x.score.header.stamp.nsecs))
      _x = self.score.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2bf3I().pack(_x.score.drone_id, _x.score.task_id, _x.score.score, _x.task.header.seq, _x.task.header.stamp.secs, _x.task.header.stamp.nsecs))
      _x = self.task.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_b3I().pack(_x.task.task_id, _x.task.task_geometry.header.seq, _x.task.task_geometry.header.stamp.secs, _x.task.task_geometry.header.stamp.nsecs))
      _x = self.task.task_geometry.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2df2b().pack(_x.task.task_geometry.lat, _x.task.task_geometry.lon, _x.task.task_geometry.alt, _x.task.allocated, _x.task.type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_geometry is None:
        self.drone_geometry = behaviour.msg.drone_geometry()
      if self.score is None:
        self.score = behaviour.msg.score()
      if self.task is None:
        self.task = behaviour.msg.task()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 23
      (_x.drone_id, _x.mode, _x.type, _x.messagetime, _x.drone_geometry.header.seq, _x.drone_geometry.header.stamp.secs, _x.drone_geometry.header.stamp.nsecs,) = _get_struct_3bd3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.drone_geometry.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.drone_geometry.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 46
      (_x.drone_geometry.lat, _x.drone_geometry.lon, _x.drone_geometry.alt, _x.drone_geometry.yaw, _x.drone_geometry.roll, _x.drone_geometry.pitch, _x.battery, _x.drone_soh, _x.score.header.seq, _x.score.header.stamp.secs, _x.score.header.stamp.nsecs,) = _get_struct_2d4f2b3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.score.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.score.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 18
      (_x.score.drone_id, _x.score.task_id, _x.score.score, _x.task.header.seq, _x.task.header.stamp.secs, _x.task.header.stamp.nsecs,) = _get_struct_2bf3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.task.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.task.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.task.task_id, _x.task.task_geometry.header.seq, _x.task.task_geometry.header.stamp.secs, _x.task.task_geometry.header.stamp.nsecs,) = _get_struct_b3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.task.task_geometry.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.task.task_geometry.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 22
      (_x.task.task_geometry.lat, _x.task.task_geometry.lon, _x.task.task_geometry.alt, _x.task.allocated, _x.task.type,) = _get_struct_2df2b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3bd3I().pack(_x.drone_id, _x.mode, _x.type, _x.messagetime, _x.drone_geometry.header.seq, _x.drone_geometry.header.stamp.secs, _x.drone_geometry.header.stamp.nsecs))
      _x = self.drone_geometry.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d4f2b3I().pack(_x.drone_geometry.lat, _x.drone_geometry.lon, _x.drone_geometry.alt, _x.drone_geometry.yaw, _x.drone_geometry.roll, _x.drone_geometry.pitch, _x.battery, _x.drone_soh, _x.score.header.seq, _x.score.header.stamp.secs, _x.score.header.stamp.nsecs))
      _x = self.score.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2bf3I().pack(_x.score.drone_id, _x.score.task_id, _x.score.score, _x.task.header.seq, _x.task.header.stamp.secs, _x.task.header.stamp.nsecs))
      _x = self.task.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_b3I().pack(_x.task.task_id, _x.task.task_geometry.header.seq, _x.task.task_geometry.header.stamp.secs, _x.task.task_geometry.header.stamp.nsecs))
      _x = self.task.task_geometry.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2df2b().pack(_x.task.task_geometry.lat, _x.task.task_geometry.lon, _x.task.task_geometry.alt, _x.task.allocated, _x.task.type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.drone_geometry is None:
        self.drone_geometry = behaviour.msg.drone_geometry()
      if self.score is None:
        self.score = behaviour.msg.score()
      if self.task is None:
        self.task = behaviour.msg.task()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 23
      (_x.drone_id, _x.mode, _x.type, _x.messagetime, _x.drone_geometry.header.seq, _x.drone_geometry.header.stamp.secs, _x.drone_geometry.header.stamp.nsecs,) = _get_struct_3bd3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.drone_geometry.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.drone_geometry.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 46
      (_x.drone_geometry.lat, _x.drone_geometry.lon, _x.drone_geometry.alt, _x.drone_geometry.yaw, _x.drone_geometry.roll, _x.drone_geometry.pitch, _x.battery, _x.drone_soh, _x.score.header.seq, _x.score.header.stamp.secs, _x.score.header.stamp.nsecs,) = _get_struct_2d4f2b3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.score.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.score.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 18
      (_x.score.drone_id, _x.score.task_id, _x.score.score, _x.task.header.seq, _x.task.header.stamp.secs, _x.task.header.stamp.nsecs,) = _get_struct_2bf3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.task.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.task.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.task.task_id, _x.task.task_geometry.header.seq, _x.task.task_geometry.header.stamp.secs, _x.task.task_geometry.header.stamp.nsecs,) = _get_struct_b3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.task.task_geometry.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.task.task_geometry.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 22
      (_x.task.task_geometry.lat, _x.task.task_geometry.lon, _x.task.task_geometry.alt, _x.task.allocated, _x.task.type,) = _get_struct_2df2b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2bf3I = None
def _get_struct_2bf3I():
    global _struct_2bf3I
    if _struct_2bf3I is None:
        _struct_2bf3I = struct.Struct("<2bf3I")
    return _struct_2bf3I
_struct_2d4f2b3I = None
def _get_struct_2d4f2b3I():
    global _struct_2d4f2b3I
    if _struct_2d4f2b3I is None:
        _struct_2d4f2b3I = struct.Struct("<2d4f2b3I")
    return _struct_2d4f2b3I
_struct_2df2b = None
def _get_struct_2df2b():
    global _struct_2df2b
    if _struct_2df2b is None:
        _struct_2df2b = struct.Struct("<2df2b")
    return _struct_2df2b
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3bd3I = None
def _get_struct_3bd3I():
    global _struct_3bd3I
    if _struct_3bd3I is None:
        _struct_3bd3I = struct.Struct("<3bd3I")
    return _struct_3bd3I
_struct_b3I = None
def _get_struct_b3I():
    global _struct_b3I
    if _struct_b3I is None:
        _struct_b3I = struct.Struct("<b3I")
    return _struct_b3I