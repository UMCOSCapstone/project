import configparser
import json
import requests
import random

class Sensor():

    name = ""
    baudRate = 0
    serial = ""
    port = ""
    status = ""
    id = 0

    def __init__(self, name, baudRate, serial, port, status, id):
        self.name = name
        self.baudRate = baudRate
        self.serial = serial
        self.port = port
        self.status = status
        self.id = id

    def toJSON(self):
        return {"name": self.name, "baudRate": self.baudRate, "serial": self.serial, "port": self.port, "status": self.status, "id": self.id}

    def __hash__(self):
        return self.id

    def __repr__(self):
        return "name: {0} baud rate: {1} serial: {2} port: {3} status: {4} id:{5}".format(self.name, self.baudRate, self.serial, self.port, self.status, self.id)


class SensorManager():

        def updateRemoteConfig(self):

            config = configparser.ConfigParser()
            config.read('config.ini')

            try:
                url = config['DEFAULT']['secondaryaddress']

                headers = {'content-type': 'application/json'}

                response = requests.post("http://" + url + "/updateSensors", data=json.dumps(config['DEFAULT']["sensors"]), headers=headers)

                if(response.status_code == requests.codes.ok):
                    print("Successfully Sent Data")
                else:
                    print("Error Submitting")
            except:
                print("Error: Could not reach server")

        def add(self, sensor):
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            jsonSensors.append({"name": sensor.name, "baudRate": sensor.baudRate, "serial": sensor.serial, "port": sensor.port, "status": sensor.status, "id": sensor.id})

            config.set('DEFAULT', 'sensors', json.dumps(jsonSensors, indent=4))
            config.write(open("config.ini", "w"))
            self.updateRemoteConfig()

        def remove(self, sensor):
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            newSensorJson = []
            for jsonSensor in jsonSensors:
                if(jsonSensor["id"] != sensor.id):
                    newSensorJson.append(jsonSensor)

            config.set('DEFAULT', 'sensors', json.dumps(newSensorJson, indent=4))
            config.write(open("config.ini", "w"))
            self.updateRemoteConfig()


        def update(self, sensor):
            print("updating being called")
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            for jsonSensor in jsonSensors:
                if(jsonSensor["id"] == sensor.id):
                    jsonSensor["name"] = sensor.name
                    jsonSensor["baudRate"] = sensor.baudRate
                    jsonSensor["serial"] = sensor.serial
                    jsonSensor["port"] = sensor.port
                    jsonSensor["status"] = sensor.status
                    jsonSensor["id"] = sensor.id

            config.set('DEFAULT', 'sensors', json.dumps(jsonSensors, indent=4))
            config.write(open("config.ini", "w"))
            self.updateRemoteConfig()

        def get(self):
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            sensorArray = []

            for jsonSensor in jsonSensors:
                s = Sensor(jsonSensor["name"], jsonSensor["baudRate"], jsonSensor["serial"], jsonSensor["port"], jsonSensor["status"], jsonSensor["id"])
                sensorArray.append(s)

            return sensorArray

# sm = SensorManager()
#
# sen = Sensor("Jacob", 21, "Wood", "22")
#
# print(sm.get())
# print("\n")
# sm.add(sen)
# print(sm.get())
# print("\n")
# sen.name = "jack"
# sm.update(sen)
# print(sm.get())
# print("\n")
# sm.remove(sen)
# print(sm.get())
