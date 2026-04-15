#!/usr/bin/env python

# ==============================================================================
# MIT License
#
# Copyright (c) 2023-2025 Institute for Automotive Engineering (ika), RWTH Aachen University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

import rclpy
from rclpy.node import Node
from etsi_its_srem_ts_msgs.msg import *
import utils


class Publisher(Node):

    def __init__(self):

        super().__init__("srem_ts_publisher")
        topic = "/etsi_its_conversion/srem_ts/in"
        self.publisher = self.create_publisher(SREM, topic, 1)
        self.timer = self.create_timer(1.0, self.publish)

    def publish(self):

        msg = SREM()

        msg.header.protocol_version = 2
        msg.header.message_id = msg.header.MESSAGE_ID_SREM
        msg.header.station_id.value = 100
        
        msg.srm.second.value = int(self.get_clock().now().nanoseconds * 1e-6) % int(60*1e3) # Current milliseconds in the last minute.
        
        msg.srm.requestor.id.choice = msg.srm.requestor.id.CHOICE_STATION_ID
        msg.srm.requestor.id.station_id.value = 100

        self.get_logger().info(f"Publishing SREM (TS)")
        self.publisher.publish(msg)


if __name__ == "__main__":

    rclpy.init()
    publisher = Publisher()
    rclpy.spin(publisher)
    rclpy.shutdown()
