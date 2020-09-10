#!/usr/bin/env python
# license removed for brevity
from __future__ import print_function
from std_msgs.msg import String
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import psutil
import string
import random
import rospy
import time


def on_connect(client, userdata, flags, rc):
    print("connected with code " + str(rc))
    client.subscribe("Tutorial2/#")


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    print("message received")


# The callback for when a PUBLISH message is received from the server.
def on_message2(client, userdata, msg):
    print("Message received-> " + msg.topic + " " +
          str(msg.payload))  # Print a received msg
    if msg.payload.decode() == "prova":
        print("Yes!")


def on_log(client, userdata, level, buf):
    print("log: ", buf)


def on_prova():
    print("prova")


def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))


def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + "Dati ricevuti %s", data.data)
    print("dati ricevuti 1 " + data.data)
    dist1 = data.data
    invia(dist1)


def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + "Dati ricevuti %s", data.data)
    print("dati ricevuti 2 " + data.data)
    dist2 = data.data
    invia(dist2)


def invia(dist):
    client.publish("Tutorial2", "Loop publishing" + dist)


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('subscriber_cloudmqtt', anonymous=True)
    rospy.Subscriber("sensore_distanza1", String, callback1)
    rospy.Subscriber("sensore_distanza2", String, callback2)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message2

client.username_pw_set("fkjqkoul", "wK0aUWpQWS35")
client.connect("tailor.cloudmqtt.com", 16434, 60)
client.subscribe("Tutorial2/#", 1)

client.publish("Tutorial2", "Getting started with MQTT TEST")

time.sleep(1)

dist1 = 00.00
dist2 = 00.00

if __name__ == '__main__':
    listener()
