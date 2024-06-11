#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
from custom_msgpack.msg import Infodata

class InfoTopicSubscriber(Node):

    def __init__(self):
        super().__init__('rostopic_sub')
        qos_profile = QoSProfile(depth=10)
        self.basicsrv_subscriber = self.create_subscription(
            Infodata,
            'infodata',
            self.subscribe_info_message,
            qos_profile)

    def subscribe_info_message(self, msg):
        self.get_logger().info('Received id_num:{0} id_accountnum: {0}'.format(msg.id_num, msg.account))


def main(args=None):
    rclpy.init(args=args)
    node = InfoTopicSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
