#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_turtle_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist()
move.linear.x = 0.13  # Move the robot with a linear velocity in the x axis
move.angular.z = 0.26 # Move the with an angular velocity in the z axis

while not rospy.is_shutdown():
  pub.publish(move)
  rate.sleep()


