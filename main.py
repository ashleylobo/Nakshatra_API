import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('Nakshatra-f89da92381db.json', scope)

client = gspread.authorize(creds)
sheet = client.open('Nakshtra 0.4').sheet1
telemedicine = sheet.get_all_records()



pp = pprint.PrettyPrinter()
def csvToJson():
    l=[]
    for i in range(0,55):
        l.append(telemedicine[i])
    return l
print(str(csvToJson()))