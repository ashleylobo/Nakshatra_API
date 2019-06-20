import flask
import os
from flask import jsonify, request
from flask import flash, redirect, url_for, session

from flask_cors import CORS, cross_origin
import requests, json
import pandas as pd
import requests









app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
cors = CORS(app, resources={r"/*": {"origins": "*"}})






"""
Index(['Temperature (C)', 'Humidity', 'Wind Speed (km/h)',
       'Wind Bearing (degrees)', 'Visibility (km)', 'Pressure (millibars)',
       'Summary'],
"""





@app.route('/predict', methods=['POST'])
def predict():
	return "blo"



@app.route('/', methods=['GET'])
def home():
    print("loaded")
    return "Welcome to My API"





app.run(host='0.0.0.0',port=5000)
