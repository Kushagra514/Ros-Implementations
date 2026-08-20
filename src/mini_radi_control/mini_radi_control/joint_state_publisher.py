import rclpy 
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointStatePublisher(Node):

    def __init__(self):
        super().__init__("mini_radi_joint_state_publisher")

        self.publisher = self.create_publisher(
            JointState,
            "/joint_states",
            10
        )

        self.timer = self.create_timer(
            0.05,
            self.publish_joint_states
        )
        self.angle = 0.0

    def publish_joint_states(self):
        msg = JointState()

        msg.header.stamp = self.get_clock().now().to_msg()

        msg.name = [
            "left_wheel_joint",
            "right_wheel_joint"
            ]

        msg.position = [
            self.angle,
            self.angle
            ]

        self.publisher.publish(msg)
        self.angle += 0.01


def main(args = None):
    rclpy.init(args = args)
    node = JointStatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()