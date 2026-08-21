from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    # world path
    world = PathJoinSubstitution([
        FindPackageShare("mini_radi_gazebo"),
        "worlds",
        "mini_radi.world"
    ])

    # URDF path
    urdf_file = PathJoinSubstitution([
        FindPackageShare("mini_radi_description"),
        "urdf",
        "mini_radi.urdf"
    ])

    # Read URDF
    robot_description = ParameterValue(
        Command(["cat ", urdf_file]),
        value_type=str
    )

    # Start Gazebo
    gazebo = ExecuteProcess(
        cmd=[
            "gazebo",
            "--verbose",
            "-s", "libgazebo_ros_init.so",
            "-s", "libgazebo_ros_factory.so",
            world
        ],
        output="screen"
    )

    # Publish TF
    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {"robot_description": robot_description}
        ]
    )

    # Joint states
    joint_state_publisher = Node(
        package="mini_radi_control",
        executable="joint_state_publisher"
    )

    # Spawn robot into Gazebo
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity", "mini_radi",
            "-topic", "robot_description",
            "-z", "0.5"
        ],
        output="screen"
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        joint_state_publisher
    ])