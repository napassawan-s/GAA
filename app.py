from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
import logging

# tensorflow
import tensorflow as tf
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
model = tf.keras.models.load_model('model/84866.hdf5')

def model_predict(img_path,model):

  #decoded = tf.io.decode_base64(imgBase64)
    img_path = 'Metal_0.jpg'
    img = image.load_img(img_path,target_size=(180,180))
    #Preprocessing the image
    x=image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    result = model.predict(x)
    print('this is result jaaaaa ', result)
    prediction = ''

    if result[0][0] == 1:
       prediction = 'Glass'
    elif result[0][1] == 1:
      prediction = 'Metal'
    elif result[0][2] == 1:
      prediction = 'Paper'
    else:
      prediction = 'Plastic'
    return prediction

@app.route('/',methods=['GET'])
def index():
    # Main page
    return 'HAHA'

@app.route("/send", methods=["POST"], strict_slashes=False)
def add_articles():
    return request

@app.route("/testpred", methods=["GET"])
def test():
  example = 'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII='
  preds = model_predict(example,model)
  return preds

@app.route('/predict', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
      json = [{ 'uniqueId': 'Glass', 'title': 'Glass','pic': [] }, { 'uniqueId': 'Metal', 'Metal': 'Glass','pic': [] }, { 'uniqueId': 'Paper', 'title': 'Paper','pic': [] }, { 'uniqueId': 'Plastic', 'title': 'Plastic','pic': [] }]
        # Get each pic from recieved JSON
        #f = request.files['file']

        #save the file ./uploads (?)
        #basepath = os.path.dirname(__file__)
        #file_path = os.path.join(basepath,'uploads',secure_filename(f.filename))
        #f.save(file_path)
      request_data = request.get_json()
      for items in request_data:
          preds = model_predict(items['base64'],model)
          
          #className = 0
          #convert predict result to 0,1,2,3 return in class val

          json[preds]['pic'].append({'width': items['width'], 'height': items['height'], 'uri': items['uri'] })
        
        # have to loop each photo then store class, image (base64,uri), original height, original width as JSON in array format =>
        # { uniqueId: 'Glass',
        # title: 'Glass',
        # pic: [{width: 200, height: 300, uri:"", base64: }]
        # }
        # make prediction
        

      return json
    return None

if __name__ == '__main__':

    #app.run(port=5002, debug=True)
    
    #app.run(host="192.168.29.186", port=800, debug=False)

    app.run(port=5000)

