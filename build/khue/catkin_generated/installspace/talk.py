import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publischer('chatte', String,queue_size =10)// ham gui message voi ten chatte
	rospy.init_node('takler', anonymous =True)
	rate =rospy.Rate(10)#10hz
	while not rospy.is_shuthown():
		hello_str = "hello world %s" %rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()

if__name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
