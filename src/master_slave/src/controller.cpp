#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <turtlesim/Pose.h>

float linx, angZ;

void filterVelocityCallback(const geometry_msgs::Twist& msg){
   linx = msg.linear.x;      angZ = msg.angular.z;
}

int main(int argc, char **argv){
  ros::init(argc, argv, "filter_velocity");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("/tb3_0/cmd_vel",1000,&filterVelocityCallback);
  ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/tb3_1/cmd_vel", 1000);
  ros::Rate rate(2);

  while(ros::ok()){
     geometry_msgs::Twist msg;
     msg.linear.x = linx;     msg.angular.z = angZ;
        ROS_INFO_STREAM("Subscriber velocities:"<<" linear="<<linx<<" angular="<<angZ);
        pub.publish(msg);   
   
     rate.sleep();
     ros::spinOnce();      
  } 
}