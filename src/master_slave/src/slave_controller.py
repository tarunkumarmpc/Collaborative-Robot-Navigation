#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from std_msgs.msg import String
import numpy as np
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped

global position_tb3_0_x
global position_tb3_0_y 
global oriention_tb3_0 
position_tb3_0_x = 0
position_tb3_0_y = 0
oriention_tb3_0  = 0
global quat_tb3_0
prev_transformed = [[0], [0], [1]]
def callback(data):
    print "New message received"

    global position_tb3_0_x
    global position_tb3_0_y
    global quat_tb3_0
    position_tb3_0 = data.pose.pose.position
    quat_tb3_0 = data.pose.pose.orientation
    oriention_tb3_0 = data.pose.pose.orientation.w
    position_tb3_0_x = position_tb3_0.x
    position_tb3_0_y = position_tb3_0.y

def timer_callback(event):
     
    global position_tb3_0_x
    global position_tb3_0_y
    global quat_tb3_0
    goal = PoseStamped()
    goal.header.seq = 1
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"
    tr = [[1, 0, -0.5], [0, 1, -0.3], [0, 0,1]]
    rb = [[position_tb3_0_x], [position_tb3_0_y], [1]]
    transformed = np.dot(tr,rb)
    print(transformed)
    if transformed[0] != prev_transformed[0] or transformed[1] != prev_transformed[1] :

	    goal.pose.position.x = transformed[0]
	    goal.pose.position.y = transformed[1]
	    
	    goal.pose.orientation = quat_tb3_0

	    goal.pose.orientation.w = oriention_tb3_0
	    print " timer Running"
	    goal_publisher = rospy.Publisher("tb3_1/move_base_simple/goal", PoseStamped, queue_size=5)
	    goal_publisher.publish(goal)
	    prev_transformed[0]  = transformed[0]
            prev_transformed[1]  = transformed[1]


def listener():

    rospy.init_node('control', anonymous=True)

    rospy.Subscriber('/tb3_0/amcl_pose', PoseWithCovarianceStamped, callback)
    timer = rospy.Timer(rospy.Duration(2), timer_callback)

    rospy.spin()    
 

if __name__ == '__main__':
    print "Running"
    listener()
