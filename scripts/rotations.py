#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import tf

if __name__ == '__main__':

    # Define Euler angles
    roll = math.radians(30)
    pitch = math.radians(42)
    yaw = math.radians(58)

    # Convert Euler angles to Quaternion
    print("Euler angle to Quaternion")
    q = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
    print("Quaternion: {}".format(q))

    print("")

    # Convert Quaternion to Euler angles
    print("Quaternion to Euler angle")
    r, p, y = tf.transformations.euler_from_quaternion(q)
    print("Euler angle: ({}, {}, {})".format(math.degrees(r), math.degrees(p), math.degrees(y)))
