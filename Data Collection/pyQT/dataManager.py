import requests
import json
import datetime
from flask_socketio import SocketIO, emit
from flask import Flask
from threading import Thread
import json

url = 'http://localhost:5000/send'
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

def sendData(sensorName, dataType):
    print("Calling: sendData()")

    jsonData = {"name": sensorName, "serialNumber": "1234", "dataType": "bin", "data": dat[sensorName]}

    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(jsonData), headers=headers)

    if(response.status_code == requests.codes.ok):
        # clear data
        dat[sensorName].clear()
        print("Successfully Sent Data")
    else:
        print("Error Submitting")
    # else:
    #     print("not here")




def addData(sensor, data, dataType):
    print("adding data")
    # print(value[14])

    dateTime = datetime.datetime.now()
    try:
        # print(json.dumps(data))
        socketio.emit('newnumber', {'data': data, 'sensor': sensor.toJSON(), "dateTime": str(dateTime)}, namespace='/test')
    except:
        print("Socket Error occured")
    # socketio.emit('newnumber', {'number': 1}, namespace='/test')

    # data type txt or bin

    # START OF COMMENT OUT

    # print("Calling: addData()")
    #
    #
    # found = False
    #
    # if not (sensorName in dat):
    #     dat[sensorName] = []
    #
    # dat[sensorName].append({"value": value, "time": str(dateTime)})
    #
    # open(sensorName + "." + dataType, "a").write(value)

    # END OF COMMENT OUT

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
