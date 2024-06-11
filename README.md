# rsaem_ros2_basic

https://drive.google.com/file/d/1VAbHFt9c2Rku92v30xDB8SwsaRMi1u_F/view?usp=sharing
에서 다운로드 받은 후 폴더들은 ros2_ws/src 아래로 복사하고 나서 colcon build 해주세요.

# ros2_basic_test 

colcon build --packages-select ros2_basic_test

source /home/nvidia/ros2_ws/install/setup.bash

ros2 run ros2_basic_test rostopic_pub

ros2 run ros2_basic_test rostopic_sub

--------------------------

# custom_msgpack 

colcon build --packages-select custom_msgpack

--------------------------

# ros2_basic_topicmsg 

colcon build --packages-select ros2_basic_topicmsg


ros2 run ros2_basic_topicmsg info_publisher

ros2 run ros2_basic_topicmsg info_subscriber

-----------------

# ros2_basic_service

colcon build --packages-select ros2_basic_service

ros2 run ros2_basic_service srv_server

ros2 run ros2_basic_service srv_client

-----------------

# ros2_basic_action

colcon build --packages-select ros2_basic_action

ros2 run ros2_basic_action simple_action_server

ros2 run ros2_basic_action simple_action_client

------------

ros2 launch ros2_basic_test basic_test_launch.py




