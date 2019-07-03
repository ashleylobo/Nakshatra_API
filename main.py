import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('Nakshatra-f89da92381db.json', scope)

client = gspread.authorize(creds)
sheet = client.open('Nakshtra 0.4').sheet1
telemedicine = sheet.get_all_records()



def csvToJson():
    #mapping=telemedicine[0]

    data={}
    for i in range(1,len(telemedicine)):
        if(telemedicine[i]['nakshtra'] in data.keys()):
            data[telemedicine[i]['nakshtra']].append(telemedicine[i])
        else:
            data[telemedicine[i]['nakshtra']]=[telemedicine[i]]
    return data

def csvToDay():
    data={}
    for i in range(1,len(telemedicine)):
        if(telemedicine[i]['nakshtra'] in data.keys()):
            data[telemedicine[i]['nakshtra']].append(telemedicine[i])
        else:
            data[telemedicine[i]['nakshtra']]=[telemedicine[i]]
    return data
