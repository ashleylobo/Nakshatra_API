import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('Nakshatra-f89da92381db.json', scope)

client = gspread.authorize(creds)




def csvToJson():
    #mapping=telemedicine[0]
    sheet = client.open('Nakshtra 0.4').sheet1
    telemedicine = sheet.get_all_records()
    data={}
    for i in range(1,len(telemedicine)):
        if(telemedicine[i]['Value_0'] in data.keys()):
            data[telemedicine[i]['Value_0']].append(telemedicine[i])
        else:
            data[telemedicine[i]['Value_0']]=[telemedicine[i]]
    return data
