#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim
#
# spin_until_future_complete() 방식
# - 서비스 요청 후, 응답이 올 때까지 코드가 그 자리에서 "절차적으로" 대기합니다.
# - 응답 결과가 바로 다음 줄에서 필요한 경우에 적합합니다.

from custom_msgpack.srv import WordCount

import rclpy
from rclpy.node import Node


class BasicClient(Node):

    def __init__(self):
        super().__init__('srv_client')
        self.cli = self.create_client(WordCount, 'word_count')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = WordCount.Request()

    def send_request(self):
        self.req.words = "Hello ROS World"
        self.future = self.cli.call_async(self.req)

        # 응답이 도착할 때까지 여기서 대기(spin)한 뒤 다음 코드로 진행
        rclpy.spin_until_future_complete(self, self.future)

        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    basic_client = BasicClient()
    response = basic_client.send_request()

    if response is not None:
        basic_client.get_logger().info('response: %d' % (response.count))
    else:
        basic_client.get_logger().error('service call failed')

    basic_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
