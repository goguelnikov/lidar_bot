import os
from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():


    # Include the delta2g talker
    delta2g = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    '/home/romain/Documents/delta2g/', 'run', 'talker')]),
             )

    talker_node = Node(
        package="delta2g",
        executable="talker",
    )

    rplidar = Node(
         package='rplidar_ros',
         executable='rplidar_composition',
         output='screen',
         parameters=[{
            'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.3:1.0-port0',
            'frame_id': 'laser_frame',
            'angle_compensate': True,
            'scan_mode': 'Standard'
         }]
     )
        
    return LaunchDescription([
        rplidar       
        #delta2g,
        #talker_node,
    ])
    
    
