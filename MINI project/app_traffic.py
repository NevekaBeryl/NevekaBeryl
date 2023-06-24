import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
import os
import numpy as np
import PIL.Image
from tkinter import *
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import tensorflow as tf
#from keras.applications.vgg16 import preprocess_input, decode_predictions
#from keras.models import load_model
#from keras.preprocessing.image import img_to_array, load_img


root = tk.Tk(className='Traffic light direction')
root.geometry("550x300+300+150")
root.configure(bg='lavender')
l=[]

def openfn():
    filename = filedialog.askopenfilename()
    l.append(filename)
    return filename
def open_img():
    x = openfn()
    img = PIL.Image.open(x)
    img = img.resize((400,200))
    img.thumbnail(((root.winfo_width()/5),root.winfo_height()/5))
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()


upload2=Button(root, text="Upload an image",command=open_img,
            padx=0.2,pady=2)

upload2.configure(background='#364156', foreground='white',
        font=('arial',10,'bold'))

upload2.place(x=300, y=350)



def classify(l):
    vehicle_list = []
    for img_path in l:
        im = cv2.imread(img_path)
        #print(im.shape)

        bbox, label, conf = cv.detect_common_objects(im)

        output_image = draw_bbox(im, bbox, label, conf)
        #plt.imshow(output_image)
        #plt.show()
        #image = load_img(img_path, target_size=(100, 100))
        #image = img_to_array(image)
        #image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        #image = preprocess_input(image)
        #im = image 
        N_car = label.count('car')
        N_bus = label.count('bus')
        N_motorcycle = label.count('motorcycle')
        N_truck = label.count('truck')
        vehicle = N_bus + N_car + N_motorcycle + N_truck
        vehicle_list.append(vehicle)
    print(vehicle_list)
    mini = min(vehicle_list)
    ind_mini = vehicle_list.index(mini)
    print(mini)
    
    if ind_mini == 0:
        btn = Button(root, text="NORTH",padx=10,pady=0.2) 
        btn.configure(background = '#364156', foreground='white',font=('arial',10,'bold'))
        btn.place(x=1150,y=450)
    elif ind_mini == 1:
        btn = Button(root, text="EAST",padx=0.2,pady=2) 
        btn.configure(background = '#364156', foreground='white',font=('arial',10,'bold'))
        btn.place(x=1150,y=450)
    elif ind_mini == 2:
        btn = Button(root, text="SOUTH",padx=15,pady=2) 
        btn.configure(background = 'dark orchid', foreground='white',font=('arial',10,'bold'))
        btn.place(x=1150,y=450)
    elif ind_mini == 3:
        btn = Button(root, text="WEST",padx=0.2,pady=2) 
        btn.configure(background = '#364156', foreground='white',font=('arial',10,'bold'))
        btn.place(x=1100,y=450)

def show_classify_button():
    classify_b=Button(root,text="predict Vehicles",
    command=lambda: classify(l),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
    font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)


show_classify_button()
heading = Label(root, text="Traffic Signal Optimisation",pady=20, font=('arial',20,'bold'))

heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()


root.mainloop()
