#install the below modules by using pip install command in command prompt
#importing modules into program

""" opencv is used for all sort of images and videos analysis like facial recognition and detection.
    opencv is used to read the image in the form of multi-dimentional array """
import cv2

""" ploting library for the python programming. for ploting the image with boxes"""
import matplotlib.pyplot as plt

""" cvlib is a computer vision libraray, used to detect the objects"""
import cvlib as cv

""" imported for drawing boxes"""
from cvlib.object_detection import draw_bbox

#read the image and convert it into gray scale image
im = cv2.imread('parking1.jpg')
#im = cv2.imread('traffic_img1.png')
#print(im)


#perform object detection on the image
bbox, label, conf = cv.detect_common_objects(im)


#display the image with a bounding box and label about the detected objects
output_image = draw_bbox(im, bbox, label, conf)


#creating an object to display the output_image
plt.imshow(output_image)


#display the output image
plt.show()


#counting number of cars present in the image
N_car=label.count('car')


#counting number of busses present in the image
N_bus=label.count('bus')


#counting number of motorcycles present in the image
N_motorcycle=label.count('motorcycle')

N_truck=label.count('truck')

#calculating number of vehicle
vehicle= N_bus + N_car + N_motorcycle+N_truck

#displaying number of vehicle present in the image
print('Number of vehicle in the image is ',vehicle)

#calculating time required depending upon the vehicles and displaying
if vehicle<=55:
    print("Time displayed in signal Indicator is ",vehicle+5)
else:
   print("Time displayed in signal Indicator is ",60)
