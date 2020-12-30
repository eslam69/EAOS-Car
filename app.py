import cv2
import os
from flask import Flask, request,flash, redirect,url_for
from core import *


app = Flask(__name__, static_url_path='/static')
direction = "F"
state = "wait"

@app.route('/')
def index():
    return """<body style="background-color:powderblue;"> <h1 style=" color:red;font-family: verdana;">EOAS Car Server </h1>"""
    
@app.route("/frame", methods=["POST","GET"])
def process_posted_image():

    if request.method == 'POST':

        if 'image' not in request.files:

            flash('No file part')
            return redirect(url_for('index'))
        file_bytes = request.files['image']
        file_bytes.save('static/frame.jpg')
        cv_image = cv2.imread('frame.jpg')
        global direction
        direction = compute_direction(cv_image)
        print(direction)
        return 'done!'
    if request.method == 'GET':
        if "frame.jpg" in os.listdir('static/'):
            print("found")
            return """ <img src="static\frame.jpg" alt="last frame"> """
        else:
            return "No Frames :("

@app.route('/direction', methods=['GET','POST'])
def Direction():
    global direction
    if request.method == 'GET':
        return direction
    else: #POST
        data = request.data.decode()
        print(data)
        direction = data

@app.route('/state', methods=['GET','POST'])
def State():
    global state
    if request.method == 'GET':
        return state
    else: #POST
        data = request.data.decode()
        print(data)
        state = data

if __name__ == "__main__":
    app.debug = True
    app.run()
    
