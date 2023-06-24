import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
min_veh=0
min_time=0
max_veh=0
max_time=0
min_img=None
max_img=None

def traffic_density(image):
    global min_veh,min_time,max_veh,max_time,min_img,max_img
    im = image
    #print(im)
    time=5
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    N_car=label.count('car')
    N_bus=label.count('bus')
    N_motorcycle=label.count('motorcycle')
    N_truck=label.count('truck')
    #print(N_bus , N_car , N_motorcycle , N_truck)
    vehicle= N_bus + N_car + N_motorcycle+N_truck
    #print('Number of vehicle in the image is ',vehicle)
    if vehicle<=55:
        time+=vehicle
        print("Time displayed in signal Indicator is ",time)
    else:
        time=60
        print("Time displayed in signal Indicator is ",time)
    if vehicle>max_veh:
        max_veh=vehicle
        max_time=time
        max_img=draw_bbox(im, bbox, label, conf)
traffic_density(cv2.imread('img1.png'))
traffic_density(cv2.imread('img2.jpeg'))
traffic_density(cv2.imread('img3.jpg'))
traffic_density(cv2.imread('img4.jpg'))

print("HIGH DENSITY")
plt.imshow(max_img)
plt.show()
print('Number of vehicle in the image is ',max_veh)
print("Time displayed in signal Indicator is ",max_time)
