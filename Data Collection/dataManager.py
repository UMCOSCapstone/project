import requests
import json
import datetime

# Setting the ip of the secondary computer
url = 'http://localhost:5000/send'
dat = []

def sendData():
    headers = {'content-type': 'application/json'}

#   making a request to send the data to the secondary compuer
    response = requests.post(url, data=json.dumps(dat), headers=headers)

    if(response.status_code == requests.codes.ok):
        # clears the buffer once the data is sent
        dat.clear()
    else:
        # error sending the request
        print("Error Submitting")




def addData(sensorName, value):
    print("Calling: addData()")

#   gets the current time from the sensor
    dateTime = datetime.datetime.now()
#   if the sensor aready exitst in the dat var
    found = False

    #writes incoming data to appropriate file
    open(sensorName+".txt", "a").write(value)

#   adding the data to the dat var
    for sensor in dat:
        if(sensor["name"] == sensorName):
            found = True
            sensor["data"].append({"value": value, "time": str(dateTime)})


    if(found == False):
        sensorData = []

        sensorData.append({"value": value, "time": str(dateTime)})
        dat.append({"name": sensorName, "data": sensorData})
