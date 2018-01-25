import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
#print("Python version: \n" + sys.version)
#print("cv2 version: " + cv2.__version__)
img1 = cv2.imread('test_image_kitti.png')
hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv1)

plt.imread('test_image_kitti.png')
plt.imshow(h)
plt.show()
plt.imsave('testhue.png', h)
