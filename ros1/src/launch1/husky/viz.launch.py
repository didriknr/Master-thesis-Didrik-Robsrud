import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rqt',
            executable='rqt',
            name='rqt',
        ),
    ])


generate_launch_description()