#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatte', String,queue_size =10) # ham gui message voi ten chatte
	rospy.init_node('takler', anonymous =True)
	
	while not rospy.is_shutdown():
		hello_str = 111
		rospy.loginfo('hello time: %s', hello_str)
		pub.publish(hello_str)
		rospy.sleep(5)

if __name__ == '__main__' :
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
