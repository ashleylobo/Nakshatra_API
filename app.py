import flask
import os
from flask import jsonify, request
from flask import flash, redirect, url_for, session

from flask_cors import CORS, cross_origin
import requests, json
import pandas as pd
import requests



import gspread
from oauth2client.service_account import ServiceAccountCredentials





app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
cors = CORS(app, resources={r"/*": {"origins": "*"}})


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('Nakshatra-f89da92381db.json', scope)




client = gspread.authorize(creds)



@app.route('/getValues', methods=['GET'])
def predict():

    sheet = client.open('Nakshtra 0.4').sheet1
    telemedicine = sheet.get_all_records()
    data={}
    for i in range(1,len(telemedicine)):
        if(telemedicine[i]['Value_0'] in data.keys()):
            data[telemedicine[i]['Value_0']].append(telemedicine[i])
        else:
            data[telemedicine[i]['Value_0']]=[telemedicine[i]]
    return jsonify(data)


@app.route('/', methods=['GET'])
def home():
    print("loaded")
    return "Welcome to My AP"





if __name__ == '__main__':
    app.run()
