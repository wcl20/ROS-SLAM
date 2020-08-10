#!/usr/bin/env python

import rospy
import tf

if __name__ == '__main__':

    # Listen Transformation details from frame a to frame b
    rospy.init_node("wcl20_transform_listen", anonymous=True)
    listener = tf.TransformListener()
    rate = rospy.Rate(1.0)
    listener.waitForTransform("/frame_a", "/frame_b", rospy.Time(), rospy.Duration(1.0))
    while not rospy.is_shutdown():
        try:
            translation, quaternion = listener.lookupTransform("/frame_a", "frame_b", rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rospy.loginfo(translation)
        rospy.loginfo(quaternion)

        rate.sleep()
