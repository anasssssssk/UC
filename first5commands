# UC
--- easier way to answer questions 2-5 is ---
-> open the bag in foxglove studio.
-> go to topics.
-> here you will see all the info (topics, frequency, .msg file, etc.)

1. Create a ros2 workspace and place the exercise files in it.
   -> make a workspace dir - mkdir ros2workspace
   -> move the files to the workspace - mv rosbag2_2024_11_22-00_32_31 sysmonitor_interfaces /	home/anas/ros2workspace/

3. Determine how many topics are in the bag.
   -> ros2 bag info <bag_name>
   -> 5 topics:	/imu/acceleration
   		/imu/angular_velocity
   		/imu/data
   		/zed2i/zeed_node/left_gray/image_rect_gray
   		/system_info
 		
5. Determine the Hz of the topic image.
   -> Frequency (Hz) = no. of messages/duration
 		     = 311/10.626805833
 		     = 29.2656142
		     = 29.27 Hz approx.

7. Determine the Hz of the topic system.
 -> Frequency (Hz) = no. of messages/duration
 		= 19/10.626805833
		= 1.78793142
		= 1.79 Hz approx.

8. Determine what does the topic system return
 -> Opened and checked the .msg file
 	float64 cpu_usage
	float64 cpu_temp
	float64 ram_usage
	float64 gpu_usage
	float64 gpu_temp
	float64 gpuram_usage
 
