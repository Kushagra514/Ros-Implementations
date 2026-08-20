from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    world = PathJoinSubstitution([
        FindPackageShare("mini_radi_gazebo"),
        "worlds",
        "mini_radi.world"
    ])

    urdf_file = PathJoinSubstitution([
        FindPackageShare("mini_radi_description"),
        "urdf",
        "mini_radi.urdf"
    ])

    robot_description = ParameterValue(
        Command(["cat ", urdf_file]),
        value_type=str
    )

    gazebo = ExecuteProcess(
        cmd=[
            "gazebo",
            "--verbose",
            "-s",
            "libgazebo_ros_factory.so",
            world
        ],
        output="screen"
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {"robot_description": robot_description}
        ]
    )

    joint_state_publisher = Node(
        package="mini_radi_control",
        executable="joint_state_publisher"
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        joint_state_publisher
    ])