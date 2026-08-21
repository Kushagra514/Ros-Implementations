# Ros-Implementations

TRACK :-

Day 1 ->

- Created `mini_radi_ws` workspace and `mini_radi_description` package.
- Created the initial `mini_radi.urdf` robot model with links and joints.
- Added the URDF and RViz launch setup.
- Built the workspace using `colcon build --symlink-install`.
- Faced an issue where the robot was not visible in RViz due to the TF/Fixed Frame setup.
- Debugged `robot_description`, `robot_state_publisher`, topics, and URDF validity.
- Used `check_urdf` to verify the robot structure.
- Fixed the RViz configuration and successfully displayed the robot model.

Day 2 ->

- Created `mini_radi_control` package using `ament_python`.
- Implemented a custom `JointStatePublisher` node publishing wheel positions on `/joint_states`.
- Learned ROS 2 publishers, timers, nodes, and `JointState` messages.
- Configured `setup.py` with a `console_scripts` entry point for the Python node.
- Built and tested the package using `colcon build --symlink-install`.
- Created `mini_radi_gazebo` package and added the Gazebo world and launch configuration.
- Integrated Gazebo with `robot_state_publisher` and the custom joint-state publisher.
- Faced and debugged Gazebo startup/plugin and package installation issues.
- Added `libgazebo_ros_factory.so` to enable the `/spawn_entity` service.
- Successfully spawned `mini_radi` into Gazebo using `spawn_entity.py`.

Day 3 ->

- Tried debugging robot not spawning in gazebo did not come to a definite conclusion

Day 4 ->

- Fixed mini_radi robot spawning inside gazebo 
- spawn even though was somehow causing the robot to fall through indefinitely leading to a large -z thus although the robot was spawning we did not see the same
- tried a iterative test by spawning a static test box robot
- added a reference in mini_radi_world which eventually robot to spawn at the specified z coordinate which was z = 1.0
- apparently inertial and collision tags are necessary too for the robot to spawn got to this conclusion through reddit

