import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import psutil

class CPUTempPublisher(Node):
    def __init__(self):
        super().__init__('cpu_temp_publisher')
        self.publisher_ = self.create_publisher(Float64, '/test', 10)
        self.timer_ = self.create_timer(1.0, self.publish_cpu_temp)

    def publish_cpu_temp(self):
        temp = psutil.sensors_temperatures()['coretemp'][0].current
        msg = Float64()
        msg.data = temp
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing CPU temperature: {temp}°C')

def main(args=None):
    rclpy.init(args=args)
    cpu_temp_publisher = CPUTempPublisher()
    rclpy.spin(cpu_temp_publisher)
    cpu_temp_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
