import requests
import json

url2 = 'http://things.ubidots.com/api/v1.6/devices/angelhacks/?token=A1E-ieyMWDTtjwdcdgRwkl0DUN4rD3Yb6x'


def addData():

    dataPassed = {
        'Force': 50,
        'Pressure': 989
    }
    headers = {
        'Content-Type': 'application/json'
    }

    requestBody = json.dumps(dataPassed)
    response = requests.post(url2 , headers = headers,  json = dataPassed)
    dataRec = response.json()
    print('Post Contact Data: ')
    print(dataRec)



addData()
