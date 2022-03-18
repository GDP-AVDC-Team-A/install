// Generated by gencpp from file behaviour/score.msg
// DO NOT EDIT!


#ifndef BEHAVIOUR_MESSAGE_SCORE_H
#define BEHAVIOUR_MESSAGE_SCORE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace behaviour
{
template <class ContainerAllocator>
struct score_
{
  typedef score_<ContainerAllocator> Type;

  score_()
    : header()
    , drone_id(0)
    , task_id(0)
    , score(0.0)  {
    }
  score_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , drone_id(0)
    , task_id(0)
    , score(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int8_t _drone_id_type;
  _drone_id_type drone_id;

   typedef int8_t _task_id_type;
  _task_id_type task_id;

   typedef float _score_type;
  _score_type score;





  typedef boost::shared_ptr< ::behaviour::score_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::behaviour::score_<ContainerAllocator> const> ConstPtr;

}; // struct score_

typedef ::behaviour::score_<std::allocator<void> > score;

typedef boost::shared_ptr< ::behaviour::score > scorePtr;
typedef boost::shared_ptr< ::behaviour::score const> scoreConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::behaviour::score_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::behaviour::score_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::behaviour::score_<ContainerAllocator1> & lhs, const ::behaviour::score_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.drone_id == rhs.drone_id &&
    lhs.task_id == rhs.task_id &&
    lhs.score == rhs.score;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::behaviour::score_<ContainerAllocator1> & lhs, const ::behaviour::score_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace behaviour

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::behaviour::score_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::behaviour::score_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::behaviour::score_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::behaviour::score_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::behaviour::score_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::behaviour::score_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::behaviour::score_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f5e4a2789ac7ebf4497f97a026a84838";
  }

  static const char* value(const ::behaviour::score_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf5e4a2789ac7ebf4ULL;
  static const uint64_t static_value2 = 0x497f97a026a84838ULL;
};

template<class ContainerAllocator>
struct DataType< ::behaviour::score_<ContainerAllocator> >
{
  static const char* value()
  {
    return "behaviour/score";
  }

  static const char* value(const ::behaviour::score_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::behaviour::score_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"int8 drone_id\n"
"int8 task_id\n"
"float32 score\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::behaviour::score_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::behaviour::score_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.drone_id);
      stream.next(m.task_id);
      stream.next(m.score);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct score_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::behaviour::score_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::behaviour::score_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "drone_id: ";
    Printer<int8_t>::stream(s, indent + "  ", v.drone_id);
    s << indent << "task_id: ";
    Printer<int8_t>::stream(s, indent + "  ", v.task_id);
    s << indent << "score: ";
    Printer<float>::stream(s, indent + "  ", v.score);
  }
};

} // namespace message_operations
} // namespace ros

#endif // BEHAVIOUR_MESSAGE_SCORE_H