cmake_minimum_required(VERSION 3.5)
project(etsi_its_srem_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(msg_files
  "msg/Angle.msg"
  "msg/ApproachID.msg"
  "msg/BasicVehicleRole.msg"
  "msg/DSecond.msg"
  "msg/DeltaTime.msg"
  "msg/DescriptiveName.msg"
  "msg/Elevation.msg"
  "msg/IntersectionAccessPoint.msg"
  "msg/IntersectionID.msg"
  "msg/IntersectionReferenceID.msg"
  "msg/Iso3833VehicleType.msg"
  "msg/ItsPduHeader.msg"
  "msg/LaneConnectionID.msg"
  "msg/LaneID.msg"
  "msg/Latitude.msg"
  "msg/Longitude.msg"
  "msg/MinuteOfTheYear.msg"
  "msg/MsgCount.msg"
  "msg/Position3D.msg"
  "msg/PriorityRequestType.msg"
  "msg/RequestID.msg"
  "msg/RequestImportanceLevel.msg"
  "msg/RequestSubRole.msg"
  "msg/RequestorDescription.msg"
  "msg/RequestorPositionVector.msg"
  "msg/RequestorType.msg"
  "msg/RoadRegulatorID.msg"
  "msg/SREM.msg"
  "msg/SignalRequest.msg"
  "msg/SignalRequestList.msg"
  "msg/SignalRequestMessage.msg"
  "msg/SignalRequestPackage.msg"
  "msg/StationID.msg"
  "msg/TemporaryID.msg"
  "msg/TransitVehicleOccupancy.msg"
  "msg/TransitVehicleStatus.msg"
  "msg/TransmissionAndSpeed.msg"
  "msg/TransmissionState.msg"
  "msg/VehicleID.msg"
  "msg/VehicleType.msg"
  "msg/Velocity.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
