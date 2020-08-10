# ROS SLAM

## Setup
Install turtlebot3
```bash
cd ~/catkin_ws/src
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
git clone https://github.com/ROBOTIS-GIT/turtlebot3_autorace.git
git clone https://github.com/ros-perception/slam_gmapping.git
cd ..
rosdep install --from-paths src -i -y
catkin_make
source ~/catkin_ws/devel/setup.bash
```
Install dwa-local-planner
```bash
sudo apt-get install ros-melodic-dwa-local-planner
```

## Turtlebot3 Simulation
```bash
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_house.launch
```

## Turtlebot3 Control
In another terminal.
```bash
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
Control Robot using WASD.

## Turtlebot3 SLAM
In another terminal.
```bash
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping
```

## Gmapping Configuration
```bash
roscd turtlebot3_slam
cd config
nano gmapping_params.yaml
```

## Save Map
```bash
rosrun map_server map_saver -f ~/<map_dir>
```

## Turtlebot3 Navigation
In another terminal.
```bash
cd ~/catkin_ws
source ~/catkin_ws/devel/setup.bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=<path_to_map.yaml>
```
In RVIZ:
Use '2D Pose Estimate' Button to set initial position of robot.
Use '2D Nav Goal' Button to set goal of robot.

## Navigation Configuration
```bash
rosrun rqt_reconfigure rqt_reconfigure
```
Alternatively, setup parameters from file
```bash
roscd turtlebot3_navigation
cd param
nano dwa_local_planner_params_<model>.yaml
```

## ROS TF Package
The position of the robot wrt the odom frame is published in /odom
```bash
rostopic info odom
```
```bash
rostopic echo odom
```

The position of the robot wrt the map frame is published in /amcl_pose
```bash
rostopic info amcl_pose
```
```bash
rostopic echo amcl_pose
```

Publish information of each frame
```bash
rostopic echo tf
```

Creates a PDF file describing frames relationship
```bash
rosrun tf view_frames
```

Transformation of two frames
```bash
rosrun tf tf_echo map odom
```

Monitor transformation of frames
```bash
rosrun tf tf_monitor
```
```bash
rosrun tf tf_monitor map odom
```

Static Transform publisher (From frame a to Frame b)
```bash
rosrun tf static_transform_publisher <x> <y> <z> <r> <p> <y> frame_a frame_b 10
```
