import requests
import json
import datetime
from flask_socketio import SocketIO, emit
from flask import Flask
from threading import Thread
import json
import SensorManager as sm

url = 'http://141.114.192.65:5000/send'
dat = {}

status = 1

app = Flask(__name__)
socketio = SocketIO(app)

def initSocket():

    @socketio.on('connect', namespace='/test')
    def test_connect():
        # need visibility of the global thread object
        print('Client connected')


    @socketio.on('disconnect', namespace='/test')
    def test_disconnect():
        print('Client disconnected')

    socketio.run(app, host="localhost", port=5001)

thread = Thread(target = initSocket)
thread.start()

def sendData(sensor, dataType):
    print("Calling: sendData()")

    jsonData = {"name": sensor.name, "serialNumber": sensor.serial, "dataType": "bin", "data": dat[sensor.name]}

    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(jsonData), headers=headers)

    if(response.status_code == requests.codes.ok):
        dat[sensor.name].clear()
        print("Successfully Sent Data")
    else:
        print("Error Submitting")




def addData(sensor, data, dataType):
    print("adding data")
    # print(value[14])

    dateTime = datetime.datetime.now()
    try:
        # print(json.dumps(data))
        socketio.emit('newnumber', {'data': data, 'sensor': sensor.toJSON(), "dateTime": str(dateTime)}, namespace='/test')

    except:
        print("Socket Error occured")

    found = False

    if not (sensor.name in dat):
        dat[sensor.name] = []

    dat[sensor.name].append({"value": data, "time": str(dateTime)})


    # Write to file
    # writes incoming data to appropriate file
    # if(dataType == "bin"):
    #     open(sensorName + ".bin", "ab").write(value)
    # else:
    #     open(sensorName + ".txt", "a").write(value)



    # for sensor in dat:
    #     if(sensor["name"] == sensorName):
    #         found = True
    #         sensor["data"].append({"value": value, "time": str(dateTime)})
    #
    #
    # if(found == False):
    #     sensorData = []
    #
    #     sensorData.append({"value": value, "time": str(dateTime)})
    #     dat.append({"name": sensorName, "data": sensorData})
