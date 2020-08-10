#!/usr/bin/env python

import rospy
import actionlib
import math
from actionlib_msgs.msg import *
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Point

def move_go_goal(x, y):
    # Create an action client
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    # Wait for server
    while not client.wait_for_server(rospy.Duration(5)):
        rospy.loginfo("Waiting for server ...")
    # Define goal
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position = Point(x, y, 0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0
    # Send goal to server
    client.send_goal(goal)
    # Wait for result
    client.wait_for_result(rospy.Duration(60))
    if client.get_state() == GoalStatus.SUCCEEDED:
        rospy.loginfo("Reached Goal")
        return True
    else:
        rospy.loginfo("Failed to reach Goal")
        return False


if __name__ == '__main__':
    # Navigate robot to goal position using Code
    # Start turtlebot3 Simulation and turtlebot3 Navigation 
    rospy.init_node("wcl20_navigation")
    x, y, = 0, 0
    move_go_goal(x, y)
    rospy.spin()
