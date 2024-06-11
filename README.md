# rsaem_ros2_basic

https://drive.google.com/file/d/1ircYE-FAMpE82JrVJWm0hnu_K70osRd7/view?usp=sharing

colcon build --packages-select ros2_basic_test

source /home/nvidia/ros2_ws/install/setup.bash

ros2 run ros2_basic_test rostopic_pub

ros2 run ros2_basic_test rostopic_sub

--------------------------

colcon build --packages-select custom_msgpack

colcon build --packages-select ros2_basic_topicmsg


ros2 run ros2_basic_topicmsg info_publisher

ros2 run ros2_basic_topicmsg info_subscriber

-----------------

colcon build --packages-select ros2_basic_service

ros2 run ros2_basic_service srv_server

ros2 run ros2_basic_service srv_client

-----------------

colcon build --packages-select ros2_basic_action

ros2 run ros2_basic_action simple_action_server

ros2 run ros2_basic_action simple_action_client

------------

ros2 launch ros2_basic_test basic_test_launch.py




