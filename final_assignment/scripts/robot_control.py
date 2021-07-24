#! /usr/bin/env python

import rospy
import actionlib
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from std_srvs.srv import *
from move_base_msgs.msg import MoveBaseActionGoal
from final_assignment.srv import *

x = 0
y = 0

distance_x = 0
distance_y = 0

target = Odometry()
goal_ = MoveBaseActionGoal()
#state = 0


def clbk_odom(msg):
	global x, y, target, goal, state
	   	
	x = msg.pose.pose.position.x
	y = msg.pose.pose.position.y

	state = rospy.get_param("/choice")
	
	if (state == 1):
		rospy.wait_for_service('random_target')
		
		req = random_valuesRequest()
				
		req.min = 0
		req.max = 5
		
		resp = client_random(req)		
		rospy.loginfo("Random target received [%.2f, %.2f]" % (resp.a, resp.b))	

		goal_.goal.target_pose.header.frame_id = 'map'
		goal_.goal.target_pose.pose.orientation.w = 1
		goal_.goal.target_pose.pose.position.x = resp.a
		goal_.goal.target_pose.pose.position.y = resp.b
		
		pub_goal.publish(goal_)
		
		distance_x = target.pose.pose.position.x - x
		distance_y = target.pose.pose.position.y - y

		if (distance_x > -0.1 and distance_x < 0.1) and (distance_y > -0.1 and distance_y < 0.1):
			print("Reaching the goal")
		
	elif (state == 2):
		rospy.loginfo("Choosing a target selected")

		rospy.wait_for_service('input_target')
		
		req = target_valuesRequest() 

		req.des_x = x
		req.des_y = y

		resp = client_selected(req)

		goal_.goal.target_pose.header.frame_id = 'map'
		goal_.goal.target_pose.pose.orientation.w = 1
		goal_.goal.target_pose.pose.position.x = resp.c
		goal_.goal.target_pose.pose.position.y = resp.d

		target.pose.pose.position.x = goal_.goal.target_pose.pose.position.x
		target.pose.pose.position.y = goal_.goal.target_pose.pose.position.y

		distance_x = target.pose.pose.position.x - x
		distance_y = target.pose.pose.position.y - y

		if (distance_x > -0.1 and distance_x < 0.1) and (distance_y > -0.1 and distance_y < 0.1):
			print("Reaching the goal")

		pub_goal.publish(goal_)
	
'''
	elif (state == 3):
		rospy.loginfo("following the wall selected")
		req = SetBoolRequest()
		req.data = True
		
		rospy.wait_for_service('wall_follower_switch')
		
		
	elif (state == 4):
		rospy.loginfo("Stopping in last position")
		
		goal_.goal.target_pose.header.frame_id = 'map'
		goal_.goal.target_pose.pose.orientation.w = 1
		goal_.goal.target_pose.pose.position.x = x
		goal_.goal.target_pose.pose.position.y = y
		
		pub_goal.publish(goal_)
'''		
def main():
	global pub_goal, sub, client_random, client_selected, client_wall
	rospy.init_node('robot_control')
	
	pub_goal = rospy.Publisher('move_base/goal', MoveBaseActionGoal, queue_size=1)
	sub = rospy.Subscriber('/odom', Odometry, clbk_odom)
	client_random = rospy.ServiceProxy('random_target',random_values)
	client_selected = rospy.ServiceProxy('input_target',target_values)
	client_wall = rospy.ServiceProxy('/wall_follower_switch',SetBool)
	#client_user = rospy.ServiceProxy('/interface',SetBool)
	
	rospy.spin()

if __name__ == '__main__':
    main()
