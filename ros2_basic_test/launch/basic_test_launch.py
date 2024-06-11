# ros2_basic_test
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
    
        Node(
            package='ros2_basic_test', 
            executable='rostopic_pub', 
            output='screen',
            emulate_tty=True),
        Node(
            package='ros2_basic_test', 
            executable='rostopic_sub', 
            output='screen',
            emulate_tty=True),        
    ])
