import requests
import json
import datetime

url = 'http://localhost:5000/send'
dat = {}

status = 1

def sendData(sensorName, dataType):
    status = 0
    print("Calling: sendData()")
    headers = {'content-type': 'application/json'}

    # if sensorName in dat.keys():

    print("here")

    jsonData = {"name": sensorName, "serialNumber": "1234", "dataType": "bin", "data": dat[sensorName]}

    response = requests.post(url, data=json.dumps(jsonData), headers=headers)

    if(response.status_code == requests.codes.ok):
        # clear data
        dat[sensorName].clear()
        print("Successfully Sent Data")
        status = 1
    else:
        print("Error Submitting")
        status = 1
    # else:
    #     print("not here")




def addData(sensorName, value, dataType):
    # data type txt or bin
    print("Calling: addData()")

    dateTime = datetime.datetime.now()
    found = False

    if not (sensorName in dat):
        dat[sensorName] = []

    dat[sensorName].append({"value": value, "time": str(dateTime)})

    open(sensorName + "." + dataType, "a").write(value)

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
