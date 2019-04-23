from app import app, ServerFileManager
import os
from flask import request, jsonify
import configparser
import json
import datetime

config = configparser.ConfigParser()
config.read('config.ini')
fileDirectory = config['DEFAULT']['fileDirectory']

def addData(self, sensor, data):

    date = datetime.datetime.now()

    print(data.dateTime)

    currentDirectory = fileDirectory + str(date.year) + "_" + str(date.month) + "_" + str(date.day) + "_" + str(date.hour) + "00"

    if(not os.path.isdir(currentDirectory)):
        try:
            os.mkdir(currentDirectory, 0o775)

        except:
            print("Cannot make directory")

    file = currentDirectory + "/" + sensor.name + "_" + str(sensor.serial) + ".txt"

    f = open(file, "a")
    f.write(data)

@app.route("/ping", methods=['GET'])
def ping():
    return "Hello World!"

@app.route('/send', methods=['POST'])
def send():

    sensor = request.json

    name = sensor["name"]
    data = sensor["data"]

    try:
        with open(name + ".txt", "a") as file:

            for values in data:
                print(values)
                file.write(str(values) + os.linesep)
                addData({"name": "hi", "serial": 1}, values)

            # file.close()
            print("closing: " + name + ".txt")

    except IOError as e:
        print("Couldn't open or write to file (%s)." % e)
        abort(500)


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
