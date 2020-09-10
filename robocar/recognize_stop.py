#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import cv2
import matplotlib.pyplot as plt

# Opening image
img = cv2.imread("stop1.jpg")

# OpenCV opens images as BRG
# but we want it as RGB We'll
# also need a grayscale version
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Use minSize because for not
# bothering with extra-small
# dots that would look like STOP signs
stop_data = cv2.CascadeClassifier('stop_data.xml')
found = stop_data.detectMultiScale(img_gray, minSize=(20, 20))

# Don't do anything if there's
# no sign
amount_found = len(found)


def elab(dist):
    amount_found = len(found)
    pub = rospy.Publisher('segnale', String, queue_size=10)
    rospy.init_node('recognize_stop', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        if amount_found != 0:
            # There may be more than one
            # sign in the image
            for (x, y, width, height) in found:
                # We draw a green rectangle around
                # every recognized sign
                cv2.rectangle(img_rgb, (x, y),
                              (x + height, y + width),
                              (0, 255, 0), 5)
                print(x, y)
                print('I have found one element of stop ')
                dist_str = "STOP"
                rospy.loginfo(dist_str)
                pub.publish(dist_str)
                rate.sleep()


if __name__ == '__main__':
    try:
        while True:
            elab()
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
