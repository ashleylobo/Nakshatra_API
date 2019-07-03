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






import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('Nakshatra-f89da92381db.json', scope)



app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
cors = CORS(app, resources={r"/*": {"origins": "*"}})











@app.route('/getValues', methods=['GET'])
def predict():
    client = gspread.authorize(creds)
    sheet = client.open('Nakshtra 0.4').sheet1
    telemedicine = sheet.get_all_records()
    data={}
    for i in range(1,len(telemedicine)):
        if(telemedicine[i]['nakshtra'] in data.keys()):
            data[telemedicine[i]['nakshtra']].append(telemedicine[i])
        else:
            data[telemedicine[i]['nakshtra']]=[telemedicine[i]]
    return jsonify(data)


@app.route('/getDay', methods=['GET'])
def day():
    client = gspread.authorize(creds)
    sheet = client.open('Nakshtra 0.4').sheet1
    telemedicine = sheet.get_all_records()
    data={}
    for i in range(1,len(telemedicine)):
            data[str(telemedicine[i]['gDate'])+"-"+str(telemedicine[i]['gMonth'])+"-"+str(telemedicine[i]['gYear'])]=[telemedicine[i]]
    return jsonify(data)


@app.route('/', methods=['GET'])
def home():
    client = gspread.authorize(creds)
    sheet = client.open('Nakshtra 0.4').sheet1
    telemedicine = sheet.get_all_records()
    data={}
    for i in range(1,len(telemedicine)):
            data[str(telemedicine[i]['gDate'])+"-"+str(telemedicine[i]['gMonth'])+"-"+str(telemedicine[i]['gYear'])]=[telemedicine[i]]
    return jsonify(data)




if __name__ == '__main__':
    app.run()
