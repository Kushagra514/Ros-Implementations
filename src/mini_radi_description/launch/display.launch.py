import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    package_dir = get_package_share_directory(
        "mini_radi_description"
    )

    urdf_file = os.path.join(
        package_dir,
        "urdf",
        "mini_radi.urdf"
    )

    rviz_config = os.path.join(
        package_dir,
        "rviz",
        "mini_radi.rviz"
    )

    with open(urdf_file, "r") as file:
        robot_description = file.read()

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {
                "robot_description": robot_description
            }
        ]
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=[
            "-d",
            rviz_config
        ]
    )

    return LaunchDescription([
        robot_state_publisher,
        rviz
    ])