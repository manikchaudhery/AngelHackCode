import numpy as np
import pandas as pd
import pandas
import matplotlib.pyplot as plt
import csv
import xlrd
import os
import glob
import csv
import requests
import json
import schedule
import time
import threading

from xlsxwriter.workbook import Workbook

# loading the data file
# data_file = pd.read_csv('FSRData.csv')
#
# #print (data_file[0:132])
# # create time vector from imported data
#
# time = data_file['0.0']
#
# # parse good sensor data from imported data
# sensors = data_file.ix[:, '0.0':'0.0']
# #print (sensors[0:6])

def countingFunction():
    myList = [0]
    with open('FSRData.csv') as file:
        reader = csv.reader(file)


        count = 0
        counterOfOccurences = 0
        for row in reader:
            myList.append(float(row[0]))

            if count>134:
                break
            count += 1

        print(myList)
    for x in myList:
        if x > 8.2:
            counterOfOccurences += 1
    print(counterOfOccurences)
    return  counterOfOccurences

url2 = 'http://things.ubidots.com/api/v1.6/devices/demo/?token=A1E-3nbpQ6dknoPuGAyf7k8cPXHVmj6bQN'


def addData(count):

    dataPassed = {
        'Force': count
    }
    headers = {
        'Content-Type': 'application/json'
    }

    requestBody = json.dumps(dataPassed)
    response = requests.post(url2 , headers = headers,  json = dataPassed)
    dataRec = response.json()
    print('Post Contact Data: ')
    print(dataRec)

def callerFunction():
    counterOfOccurences = countingFunction()
    if counterOfOccurences > 11:
        addData(counterOfOccurences)


def main():
    threading.Timer(10.0, main).start()
    callerFunction()

if __name__ == '__main__': main()  ##calls the main

























