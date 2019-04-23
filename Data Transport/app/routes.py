from app import app, ServerFileManager
import os
from flask import request, jsonify
import configparser
import json
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')
fileDirectory = config['DEFAULT']['fileDirectory']

def addData(sensor, data):

    date = datetime.strptime(data["time"], '%Y-%m-%d %H:%M:%S.%f')

    currentDirectory = fileDirectory + str(date.year) + "_" + str(date.month) + "_" + str(date.day) + "_" + str(date.hour) + "00"

    if(not os.path.isdir(currentDirectory)):
        try:
            os.mkdir(currentDirectory, 0o775)

        except:
            print("Cannot make directory")

    file = currentDirectory + "/" + sensor["name"] + "_" + sensor["serial"] + ".txt"

    f = open(file, "a")
    f.write(str(data["value"]) + "\n")

    return "{error: false}"

@app.route("/ping", methods=['GET'])
def ping():
    return "Hello World!"

@app.route('/send', methods=['POST'])
def send():

    req = request.json

    data = req["data"]

    for values in data:
        addData({"name": req["name"], "serial": req["serialNumber"]}, values)

    return "{success: true}"

@app.route('/updateSensors', methods=['POST'])
def updateSensors():

    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set('DEFAULT', 'sensors', request.json)
    config.write(open("config.ini", "w"))

    return json.dumps({"error": False})



@app.route('/getSensors', methods=['GET'])
def getSensors():

    config = configparser.ConfigParser()
    config.read('config.ini')
    jsonSensors = json.loads(config['DEFAULT']['sensors'])
    return json.dumps({"error": False, "sensors": jsonSensors})
