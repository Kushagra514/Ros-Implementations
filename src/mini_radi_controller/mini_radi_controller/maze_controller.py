import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class MazeController(Node):

    def __init__(self):
        super().__init__('maze_controller')

        # Controller parameters
        self.front_threshold = 0.8
        self.desired_wall_distance = 0.5
        self.kp = 1.5

        # Subscribe to LiDAR
        self.scan_subscriber = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        # Publisher for robot movement
        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

    def scan_callback(self, msg):

        # Get all LiDAR measurements
        ranges = msg.ranges

        # Extract three sectors
        front = min(ranges[350:360] + ranges[0:10])
        left = min(ranges[80:100])
        right = min(ranges[260:280])

        # Print what the robot sees
        self.get_logger().info(
            f'Front: {front:.2f} m, '
            f'Left: {left:.2f} m, '
            f'Right: {right:.2f} m'
        )

        cmd = Twist()

        if front < self.front_threshold:
            if left > right:
                cmd.linear.x = 0.0
                cmd.linear.z = 0.8
            
            else:
                cmd.linear.x = 0.0
                cmd.linear.z = -0.8
        
        else:
            error = self.desired_wall_distance - right
            cmd.linear.x = 0.4 
            cmd.angular.z = self.kp * error
        
        self.cmd_vel_publisher.publish(cmd)
        

def main(args=None):

    rclpy.init(args=args)

    node = MazeController()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()