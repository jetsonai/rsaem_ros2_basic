#!/usr/bin/env python
#
# Copyright (c) 2024 JetsonAI CO., LTD.
# Author: Kate Kim
#
# add_done_callback() 방식
# - 서비스 요청 후, 응답을 기다리지 않고 바로 다음 코드(spin)로 진행합니다.
# - 응답이 도착하면 등록해 둔 콜백 함수가 자동으로 실행됩니다.
# - 여러 서비스 요청/센서 콜백/타이머 콜백이 함께 동작해야 하는 노드에 적합합니다.

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
        # 응답이 도착하면 자동으로 response_callback이 호출되도록 등록
        self.future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info('response: %d' % (response.count))
        except Exception as e:
            self.get_logger().error('service call failed: %r' % (e,))
        finally:
            # 응답 처리가 끝났으므로 노드 종료
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    basic_client = BasicClient()
    basic_client.send_request()

    # 콜백이 호출될 때까지 노드는 계속 spin하며 다른 콜백도 함께 처리할 수 있음
    rclpy.spin(basic_client)

    basic_client.destroy_node()


if __name__ == '__main__':
    main()
