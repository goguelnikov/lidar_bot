## Lidar Robot

Lidar bot composed of :
- 1 base
- 4 motors
	- A narduino to control the motors
	- 1 L298N shield
	- to be installed : change the motors with rotation sensors
- 1 lidar
- 3 Ultrasonic sensors
- 1 camera
- 2 servos to move the camera


to do :
- install ROS2
- install joint_state_publisher
  sudo apt install ros-foxy-xacro ros-foxy-joint-state-publisher-gui
  
- install delta2g lidar
automatically launch delta2g Lidar

- instal webcam
check groups
sudo usermod -aG video $USER
sudo apt install libraspberrypi-bin v4l-utils ros-humble-v4l2-camera ros-humble-image-transport-plugins