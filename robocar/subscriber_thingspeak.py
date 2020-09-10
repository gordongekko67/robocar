#!/usr/bin/env python
# license removed for brevity
from __future__ import print_function
from std_msgs.msg import String
import paho.mqtt.publish as publish
import psutil
import string
import random
import rospy

string.alphanum = '1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1117533"

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "2TI47Y6DO8TLMUZS"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "mwa0000019203567"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "JKHSMR6BZ1KRICK3"

tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

dist1 = 00.00
dist2 = 00.00


def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + "Dati ricevuti %s", data.data)
    print("dati ricevuti 1 " + data.data)
    dist1 = data.data
    if (dist1 != 0 and dist2 != 0):
        invia(dist1, dist2)


def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + "Dati ricevuti %s", data.data)
    print("dati ricevuti 2 " + data.data)
    dist2 = data.data
    if (dist1 != 0 and dist2 != 0):
        invia(dist1, dist2)


def invia(dist1, dist2):
    #payload = "&field1=" + str(dist1)
    payload = "field1=" + str(dist1) + "&field2=" + str(dist2)
    # attempt to publish this data to the topic.
    try:
        publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort, auth={
                       'username': mqttUsername, 'password': mqttAPIKey})
        print("ho pubblicato su thingspeak!!!  field 1" + topic + payload)
    except (KeyboardInterrupt):
        print("There was an error while publishing the data.")
    except:
        print("There was an error while publishing the data.")


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('subscriber_thingspeak', anonymous=True)
    rospy.Subscriber("sensore_distanza1", String, callback1)
    rospy.Subscriber("sensore_distanza2", String, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
