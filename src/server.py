#!/usr/bin/env python

from example_posearray.srv import AddTwoInts,AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

if __name__ == "__main__":
  rospy.init_node('add_two_ints_server')
  rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
  print("Ready to add two ints.")
  rospy.spin()