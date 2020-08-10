#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
import math
import tf

def callback(msg):

    # Get quaternion from odom
    q = msg.pose.pose.orientation
    # Convert quaternion to Euler
    r, p, y = tf.transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))
    rospy.loginfo("Orientation: ({}, {}, {})".format(
        math.degrees(r),
        math.degrees(p),
        math.degrees(y)
    ))


if __name__ == '__main__':

    # Subscribe to /odom and convert quaternion to euler angles
    rospy.init_node("wcl20_orientation", anonymous=True)
    rospy.Subscriber("/odom", Odometry, callback)
    rospy.spin()
