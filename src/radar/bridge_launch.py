#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # ROS1 nodes
    roscore = Node(
        package='roscore',
        executable='roscore'
    )
    ld.add_action(roscore)

    laser_publisher = Node(
        package='laser_publisher',
        executable='laser_publisher'
    )
    ld.add_action(laser_publisher)

    # ROS2 nodes
    listener = Node(
        package='demo_nodes_cpp',
        executable='listener',
        name='my_listener',
        remappings=[
            ('/scan', 'scan')
        ]
    )
    ld.add_action(listener)

    # ROS1-ROS2 bridge node
    ros1_bridge = Node(
        package='ros1_bridge',
        executable='dynamic_bridge'
    )
    ld.add_action(ros1_bridge)

    return ld

Caught exception in launch (see debug for traceback): Caught exception when trying to load file of format [py]: __init__() missing 1 required keyword-only argument: 'node_executable'
