import os
import numpy as np
import tensorflow as tf
#from keras.applications.vgg16 import preprocess_input, decode_predictions
#from keras.models import load_model
#from keras.preprocessing.image import img_to_array, load_img
from flask import Flask, redirect, url_for, request, render_template
import matplotlib.pyplot as plt
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from werkzeug.utils import secure_filename


# define a Flask app
app = Flask(__name__)

print('Visit http://127.0.0.1:5000')

def model_predict(img_path):

    im = cv2.imread(img_path)

    bbox, label, conf = cv.detect_common_objects(im)

    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    image = load_img(img_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
   
    im =image
    
    N_car=label.count('car')

    N_bus=label.count('bus')

    N_motorcycle=label.count('Motorcycle')

    vehicle= N_bus + N_car + N_motorcycle

    '''print('Number of vehicle in the image is ',vehicle)

    #calculating time required depending upon the vehicles and displaying
    if vehicle<=55:
        print("Time displayed in signal Indicator is ",vehicle+5)
    else:
        print("Time displayed in signal Indicator is ",60)'''
    print("total vehicles :",vehicle)
    return str(vehicle)
    

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # get the file from the HTTP-POST request
        f1 = request.files['file'] 
        f2 = request.files['file1']       
        
        file1=os.path.abspath(f1.filename)
        file2=os.path.abspath(f2.filename)
  
        basepath = os.path.dirname(__file__)
        
        file_path1 = os.path.join(basepath,'uploads',secure_filename(f1.filename))
        file_path2 = os.path.join(basepath,'uploads',secure_filename(f2.filename))
    
        f1.save(file_path1)
        f2.save(file_path2)
        # make prediction about this image's class
        preds_1 = model_predict(file_path1)
        preds_2 = model_predict(file_path2)
       
        print('[RESULT]: {}'.format(preds))
        
        return preds_1+".."+preds_2
    
    return None


if __name__ == '__main__':
    app.run(port=5000, debug=True)
