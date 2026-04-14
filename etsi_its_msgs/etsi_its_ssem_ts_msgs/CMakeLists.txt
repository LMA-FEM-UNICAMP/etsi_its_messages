cmake_minimum_required(VERSION 3.5)
project(etsi_its_ssem_ts_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/ApproachID.msg"
  "msg/BasicVehicleRole.msg"
  "msg/DSecond.msg"
  "msg/IntersectionAccessPoint.msg"
  "msg/IntersectionID.msg"
  "msg/IntersectionReferenceID.msg"
  "msg/Iso3833VehicleType.msg"
  "msg/ItsPduHeader.msg"
  "msg/LaneConnectionID.msg"
  "msg/LaneID.msg"
  "msg/MinuteOfTheYear.msg"
  "msg/MsgCount.msg"
  "msg/PrioritizationResponseStatus.msg"
  "msg/RequestID.msg"
  "msg/RequestImportanceLevel.msg"
  "msg/RequestSubRole.msg"
  "msg/RequestorType.msg"
  "msg/RoadRegulatorID.msg"
  "msg/SSEM.msg"
  "msg/SignalRequesterInfo.msg"
  "msg/SignalStatus.msg"
  "msg/SignalStatusList.msg"
  "msg/SignalStatusMessage.msg"
  "msg/SignalStatusPackage.msg"
  "msg/SignalStatusPackageList.msg"
  "msg/StationID.msg"
  "msg/TemporaryID.msg"
  "msg/VehicleID.msg"
  "msg/VehicleType.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
