import requests
import json
import datetime

url = 'http://localhost:5000/send'
dat = []

def sendData():
    print("Calling: sendData()")
    headers = {'content-type': 'application/json'}


    print(json.dumps(dat))


    response = requests.post(url, data=json.dumps(dat), headers=headers)

    if(response.status_code == requests.codes.ok):
        # clear data
        dat.clear()
        print("success")
    else:
        print("Error Submitting")




def addData(sensorName, value):
    print("Calling: addData()")

    dateTime = datetime.datetime.now()
    found = False

    # Write to file


    print(json.dumps(dat))

    open(sensorName+".txt", "a").write(ser[i].readline()) #writes incoming data to appropriate file

    for sensor in dat:
        if(sensor["name"] == sensorName):
            found = True
            sensor["data"].append({"value": value, "time": str(dateTime)})


    if(found == False):
        sensorData = []

        sensorData.append({"value": value, "time": str(dateTime)})
        dat.append({"name": sensorName, "data": sensorData})
