# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from hrwros_msgs/TargetToolPoses.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class TargetToolPoses(genpy.Message):
  _md5sum = "92d21c88158c4209a26e8da56b2c4ba2"
  _type = "hrwros_msgs/TargetToolPoses"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header
geometry_msgs/PoseStamped pick_approach  # Robot tool pose right before picking
geometry_msgs/PoseStamped pick_pose      # Robot tool makes contact with the object and closes its gripper
geometry_msgs/PoseStamped pick_retreat   # Robot tool moves the object away from its resting surface
geometry_msgs/PoseStamped place_pose     # Robot tool moves object to this location and opens gripper

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
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['header','pick_approach','pick_pose','pick_retreat','place_pose']
  _slot_types = ['std_msgs/Header','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,pick_approach,pick_pose,pick_retreat,place_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TargetToolPoses, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pick_approach is None:
        self.pick_approach = geometry_msgs.msg.PoseStamped()
      if self.pick_pose is None:
        self.pick_pose = geometry_msgs.msg.PoseStamped()
      if self.pick_retreat is None:
        self.pick_retreat = geometry_msgs.msg.PoseStamped()
      if self.place_pose is None:
        self.place_pose = geometry_msgs.msg.PoseStamped()
    else:
      self.header = std_msgs.msg.Header()
      self.pick_approach = geometry_msgs.msg.PoseStamped()
      self.pick_pose = geometry_msgs.msg.PoseStamped()
      self.pick_retreat = geometry_msgs.msg.PoseStamped()
      self.place_pose = geometry_msgs.msg.PoseStamped()

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
      buff.write(_get_struct_3I().pack(_x.pick_approach.header.seq, _x.pick_approach.header.stamp.secs, _x.pick_approach.header.stamp.nsecs))
      _x = self.pick_approach.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pick_approach.pose.position.x, _x.pick_approach.pose.position.y, _x.pick_approach.pose.position.z, _x.pick_approach.pose.orientation.x, _x.pick_approach.pose.orientation.y, _x.pick_approach.pose.orientation.z, _x.pick_approach.pose.orientation.w, _x.pick_pose.header.seq, _x.pick_pose.header.stamp.secs, _x.pick_pose.header.stamp.nsecs))
      _x = self.pick_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pick_pose.pose.position.x, _x.pick_pose.pose.position.y, _x.pick_pose.pose.position.z, _x.pick_pose.pose.orientation.x, _x.pick_pose.pose.orientation.y, _x.pick_pose.pose.orientation.z, _x.pick_pose.pose.orientation.w, _x.pick_retreat.header.seq, _x.pick_retreat.header.stamp.secs, _x.pick_retreat.header.stamp.nsecs))
      _x = self.pick_retreat.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pick_retreat.pose.position.x, _x.pick_retreat.pose.position.y, _x.pick_retreat.pose.position.z, _x.pick_retreat.pose.orientation.x, _x.pick_retreat.pose.orientation.y, _x.pick_retreat.pose.orientation.z, _x.pick_retreat.pose.orientation.w, _x.place_pose.header.seq, _x.place_pose.header.stamp.secs, _x.place_pose.header.stamp.nsecs))
      _x = self.place_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.place_pose.pose.position.x, _x.place_pose.pose.position.y, _x.place_pose.pose.position.z, _x.place_pose.pose.orientation.x, _x.place_pose.pose.orientation.y, _x.place_pose.pose.orientation.z, _x.place_pose.pose.orientation.w))
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
      if self.pick_approach is None:
        self.pick_approach = geometry_msgs.msg.PoseStamped()
      if self.pick_pose is None:
        self.pick_pose = geometry_msgs.msg.PoseStamped()
      if self.pick_retreat is None:
        self.pick_retreat = geometry_msgs.msg.PoseStamped()
      if self.place_pose is None:
        self.place_pose = geometry_msgs.msg.PoseStamped()
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
      end += 12
      (_x.pick_approach.header.seq, _x.pick_approach.header.stamp.secs, _x.pick_approach.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_approach.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_approach.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pick_approach.pose.position.x, _x.pick_approach.pose.position.y, _x.pick_approach.pose.position.z, _x.pick_approach.pose.orientation.x, _x.pick_approach.pose.orientation.y, _x.pick_approach.pose.orientation.z, _x.pick_approach.pose.orientation.w, _x.pick_pose.header.seq, _x.pick_pose.header.stamp.secs, _x.pick_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pick_pose.pose.position.x, _x.pick_pose.pose.position.y, _x.pick_pose.pose.position.z, _x.pick_pose.pose.orientation.x, _x.pick_pose.pose.orientation.y, _x.pick_pose.pose.orientation.z, _x.pick_pose.pose.orientation.w, _x.pick_retreat.header.seq, _x.pick_retreat.header.stamp.secs, _x.pick_retreat.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_retreat.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_retreat.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pick_retreat.pose.position.x, _x.pick_retreat.pose.position.y, _x.pick_retreat.pose.position.z, _x.pick_retreat.pose.orientation.x, _x.pick_retreat.pose.orientation.y, _x.pick_retreat.pose.orientation.z, _x.pick_retreat.pose.orientation.w, _x.place_pose.header.seq, _x.place_pose.header.stamp.secs, _x.place_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.place_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.place_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.place_pose.pose.position.x, _x.place_pose.pose.position.y, _x.place_pose.pose.position.z, _x.place_pose.pose.orientation.x, _x.place_pose.pose.orientation.y, _x.place_pose.pose.orientation.z, _x.place_pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.pick_approach.header.seq, _x.pick_approach.header.stamp.secs, _x.pick_approach.header.stamp.nsecs))
      _x = self.pick_approach.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pick_approach.pose.position.x, _x.pick_approach.pose.position.y, _x.pick_approach.pose.position.z, _x.pick_approach.pose.orientation.x, _x.pick_approach.pose.orientation.y, _x.pick_approach.pose.orientation.z, _x.pick_approach.pose.orientation.w, _x.pick_pose.header.seq, _x.pick_pose.header.stamp.secs, _x.pick_pose.header.stamp.nsecs))
      _x = self.pick_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pick_pose.pose.position.x, _x.pick_pose.pose.position.y, _x.pick_pose.pose.position.z, _x.pick_pose.pose.orientation.x, _x.pick_pose.pose.orientation.y, _x.pick_pose.pose.orientation.z, _x.pick_pose.pose.orientation.w, _x.pick_retreat.header.seq, _x.pick_retreat.header.stamp.secs, _x.pick_retreat.header.stamp.nsecs))
      _x = self.pick_retreat.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.pick_retreat.pose.position.x, _x.pick_retreat.pose.position.y, _x.pick_retreat.pose.position.z, _x.pick_retreat.pose.orientation.x, _x.pick_retreat.pose.orientation.y, _x.pick_retreat.pose.orientation.z, _x.pick_retreat.pose.orientation.w, _x.place_pose.header.seq, _x.place_pose.header.stamp.secs, _x.place_pose.header.stamp.nsecs))
      _x = self.place_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.place_pose.pose.position.x, _x.place_pose.pose.position.y, _x.place_pose.pose.position.z, _x.place_pose.pose.orientation.x, _x.place_pose.pose.orientation.y, _x.place_pose.pose.orientation.z, _x.place_pose.pose.orientation.w))
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
      if self.pick_approach is None:
        self.pick_approach = geometry_msgs.msg.PoseStamped()
      if self.pick_pose is None:
        self.pick_pose = geometry_msgs.msg.PoseStamped()
      if self.pick_retreat is None:
        self.pick_retreat = geometry_msgs.msg.PoseStamped()
      if self.place_pose is None:
        self.place_pose = geometry_msgs.msg.PoseStamped()
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
      end += 12
      (_x.pick_approach.header.seq, _x.pick_approach.header.stamp.secs, _x.pick_approach.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_approach.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_approach.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pick_approach.pose.position.x, _x.pick_approach.pose.position.y, _x.pick_approach.pose.position.z, _x.pick_approach.pose.orientation.x, _x.pick_approach.pose.orientation.y, _x.pick_approach.pose.orientation.z, _x.pick_approach.pose.orientation.w, _x.pick_pose.header.seq, _x.pick_pose.header.stamp.secs, _x.pick_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pick_pose.pose.position.x, _x.pick_pose.pose.position.y, _x.pick_pose.pose.position.z, _x.pick_pose.pose.orientation.x, _x.pick_pose.pose.orientation.y, _x.pick_pose.pose.orientation.z, _x.pick_pose.pose.orientation.w, _x.pick_retreat.header.seq, _x.pick_retreat.header.stamp.secs, _x.pick_retreat.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pick_retreat.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pick_retreat.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.pick_retreat.pose.position.x, _x.pick_retreat.pose.position.y, _x.pick_retreat.pose.position.z, _x.pick_retreat.pose.orientation.x, _x.pick_retreat.pose.orientation.y, _x.pick_retreat.pose.orientation.z, _x.pick_retreat.pose.orientation.w, _x.place_pose.header.seq, _x.place_pose.header.stamp.secs, _x.place_pose.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.place_pose.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.place_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.place_pose.pose.position.x, _x.place_pose.pose.position.y, _x.place_pose.pose.position.z, _x.place_pose.pose.orientation.x, _x.place_pose.pose.orientation.y, _x.place_pose.pose.orientation.z, _x.place_pose.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_7d3I = None
def _get_struct_7d3I():
    global _struct_7d3I
    if _struct_7d3I is None:
        _struct_7d3I = struct.Struct("<7d3I")
    return _struct_7d3I
