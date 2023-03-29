from symbol import parameters
import math
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    # Get LIDAR parameters
    lidar_params = PathJoinSubstitution(
        [FindPackageShare('husky_group'),
        'params',
        'ouster_lidar.yaml'],
    )

    localization_params = PathJoinSubstitution(
        [FindPackageShare('husky_group'),
        'params',
        'localization.yaml'],
    )

    urdf_extras_path = PathJoinSubstitution(
                [FindPackageShare("husky_group"), "urdf", "husky_urdf_extras.urdf"]
    )

    config_husky_velocity_controller = PathJoinSubstitution(
        [FindPackageShare("husky_group"),
        "params",
        "control.yaml"],
    )
    
    # Launch the husky robot using the husky_uia uia_master_husky repo
    launch_husky_base = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution(
        [FindPackageShare("husky_base"), 'launch', 'base_launch.py'])),
        launch_arguments ={
            "urdf_extras" : urdf_extras_path,
            "localization_params" : localization_params,
            "config_husky_velocity_controller" : config_husky_velocity_controller,
        }.items()
    )


    #Launch the UM7 IMU
    node_um7_imu = Node(
        package="um7",
        executable="um7_node",
        output="screen",
    )
	
    bridge = Node(
            package='ros1_bridge',
            node_executable='dynamic_bridge',
            name='bridge'
    )



    ld = LaunchDescription()

    # Launch pointcloud to laserscan, imu and lidar
    ld.add_action(launch_ouster_lidar)

    # Launch Husky UGV
    ld.add_action(launch_husky_base)

    return ld

