import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class Subscriber1(Node):

    def __init__(self):
        super().__init__('subscriber1')
        self.subscription = self.create_subscription(
            Float64,
            '/test',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'Subscribed msg: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Subscriber1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
