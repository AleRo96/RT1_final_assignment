#! /usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from final_assignment.srv import *
import random
from array import *

def randMtoN(M,N):
	return M + (random.randint(0,10000) / (10000 / (N-M)) ) 

def myrandom(req):

	resp = random_valuesResponse()

	target_x = array('i', [-4,-4,-4,5,5,5])
	target_y = array('i', [-3,2,7,-7,-3,1])
	i = randMtoN(req.min, req.max)
	resp.a = target_x[i]	
	resp.b = target_y[i]

	rospy.loginfo("Random target generated [%.2f, %.2f]" %(resp.a, resp.b))
	return resp

def main():
   
   rospy.init_node('RandomTarget_server')
   rospy.Service('random_target', random_values, myrandom)

   rospy.spin()

if __name__ == '__main__':
	main()
