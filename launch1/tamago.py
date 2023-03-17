import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros1_bridge',
            node_executable='dynamic_bridge',
            name='bridge'
        ),

        #Node(
        #    package='demo_nodes_cpp',
        #    node_executable='listener',
        #    name='listener',
        #    remappings = [('/scan','/merge/scan')],
        #),


        #Node(
        #    package='rviz2',
        #    node_executable='rviz2',
        #    name='rviz2_open',
            #arguments=[f'-d {(os.getcwd())}/rviz/rviz2.rviz']
        #),
    ])


generate_launch_description()
