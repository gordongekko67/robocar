#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Dati ricevuti %s", data.data)
    if (data.data.startswith('Distance 1')):
        print("ricevuto 1 " + data.data)

    if (data.data.startswith('Distance 2')):
        print("ricevuto 2 " + data.data)

    if (data.data.startswith('STOP')):
        print("TROVATO UNO STOP " + data.data)


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("sensore_distanza1", String, callback)
    rospy.Subscriber("sensore_distanza2", String, callback)
    rospy.Subscriber("segnale", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
