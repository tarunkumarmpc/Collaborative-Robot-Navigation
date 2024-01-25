#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

import numpy as np

def callback(data):
    print "New message received"
   
    pub_ = rospy.Publisher('cmd_velsss', Twist)
    
    msg.linear.x = data.linear.x
    msg.angular.z = data.angular.z
    pub_.publish(msg)


def listener():

    rospy.init_node('simple_control', anonymous=True)

    rospy.Subscriber('/tb3_0/cmd_vel', Twist, callback)

    rospy.spin()    

if __name__ == '__main__':
   
    listener()
