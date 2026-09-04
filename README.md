## Edit bashrc for ROS workspace setting 

cd

gedit .bashrc

ROS_DOMAIN_ID 를 본인 번호로 바꾸어 주세요

저장

mkdir -p basic_ros2_ws/src

# rsaem_ros2_basic
git clone https://github.com/jetsonai/rsaem_ros2_basic

cd basic_ros2_ws
colcon build 

# ros2_basic_test 

colcon build --packages-select ros2_basic_test

source ~/basic_ros2_ws/install/setup.bash

ros2 run ros2_basic_test rostopic_pub

ros2 run ros2_basic_test rostopic_sub

--------------------------

# custom_msgpack 

colcon build --packages-select custom_msgpack

--------------------------

# ros2_basic_topicmsg 

colcon build --packages-select ros2_basic_topicmsg

source ~/basic_ros2_ws/install/setup.bash

ros2 run ros2_basic_topicmsg info_publisher

ros2 run ros2_basic_topicmsg info_subscriber

-----------------

# ros2_basic_service

colcon build --packages-select ros2_basic_service

source ~/basic_ros2_ws/install/setup.bash

ros2 run ros2_basic_service srv_server

ros2 run ros2_basic_service srv_client

-----------------

# ros2_basic_action

colcon build --packages-select ros2_basic_action

source ~/basic_ros2_ws/install/setup.bash

ros2 run ros2_basic_action simple_action_server

ros2 run ros2_basic_action simple_action_client

------------

ros2 launch ros2_basic_test basic_test_launch.py




