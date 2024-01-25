# Collaborative-Robot-Navigation
Autonomous and Collaborative Robot Navigation in Simulated Environments Using ROS and Gazebo


**Single robot autonomous navigation**


1)roslaunch turtlebot3_gazebo multi_turtlebot3.launch

2)roslaunch turtlebot3_slam turtlebot3_hector.launch

3)Run teleop node

r4)osrun map_server map_saver -f map (save the map)

**Multiple robot launch**

1. roslaunch turtlebot3_gazebo multi_turtlebot3.launch
2. roslaunch turtlebot3_navigation turtlebot3_navigation_tb3_0.launch
3. Give goals in the rviz

**Leader follower without any autonomous ability**

1roslaunch turtlebot3_gazebo turtlebot3_world_multi.launch

2)roslaunch turtlebot3_navigation turtlebot3_navigation_tb3_0.launch

3) rosrun master_slave controller'

**Leader follower with autonomous ability**

1. roslaunch turtlebot3_gazebo turtlebot3_world_multi.launch
2. roslaunch turtlebot3_navigation turtlebot3_navigation_multi.launch
3. rosrun master_slave slave_controller.py
Give goal on rviz
