#! /usr/bin/env python

import rospy
from std_srvs.srv import *


#state = 0

def clbk_interface():
	mystring_ = """
	1) Move randomly.
	2) Choise a target.
	3) Follow the external walls.
	4) stop in the last position."""

	while True:
		print(mystring_)
		state = int(input('Select a choice: '))
		
		if state != rospy.get_param("/choice"):
			rospy.set_param("/choice", state)

		else:
			rospy.set_param("/choice",0)

		if state >= 1 and state <= 4:
			break;
		else:
			print("Invalid statement")
	rospy.service('\interface',SetBool,clbk_interface)

def main():
	rospy.init_node('user_interface')
	
	
	return[]

        rospy.spin()

if __name__ == '__main__':
    main()
