#! /usr/bin/env python

# import ros stuff
import rospy
from std_srvs.srv import *
from final_assignment.srv import *
from nav_msgs.msg import Odometry


# service callback

def set_new_pos(req):
    print("Please insert a new position")

    resp = target_valuesResponse()

    x_goal = float(input('x goal: '))
    y_goal = float(input('y goal: '))

    resp.c = x_goal
    resp.d = y_goal

    if x_goal == -4:
	if y_goal == -3 or y_goal == 2 or y_goal == 7:
		rospy.loginfo("The target [%.2f, %.2f] is valid!" % (resp.c, resp.d))
    if x_goal == 5:
	if y_goal == -7 or y_goal == -3 or y_goal == 1:
		rospy.loginfo("The target [%.2f, %.2f] is valid!" % (resp.c, resp.d))
    else:
		rospy.loginfo("The selected target [%.2f, %.2f] is not valid. Try again" %(resp.c, resp.d))

    print("Thanks! Let's reach the next position")

    return resp


def main():
    rospy.init_node('Input_Target_server')
    rospy.Service('input_target', target_values, set_new_pos)
  
    rospy.spin()

if __name__ == '__main__':
    main()
