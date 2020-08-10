#!/usr/bin/env python

import rospy
import tf


if __name__ == '__main__':

    # Publish Transformation details from frame a to frame b
    rospy.init_node("wcl20_transform_broadcast")
    publisher = tf.TransformBroadcaster()
    rate = rospy.Rate(2)
    while not rospy.is_shutdown():
        quaternion = tf.transformations.quaternion_from_euler(0.1, 0.2, 0.3)
        translation = (1.0, 2.0, 3.0)
        time = rospy.Time.now()
        publisher.sendTransform(translation, quaternion, time, "frame_b", "frame_a")
        rate.sleep()
