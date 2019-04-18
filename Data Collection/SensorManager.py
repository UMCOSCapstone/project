import configparser
import json

class Sensor():

    name = ""
    baudRate = 0
    serial = ""
    port = ""
    status = ""

    def __init__(self, name, baudRate, serial, port, status):
        self.name = name
        self.baudRate = baudRate
        self.serial = serial
        self.port = port
        self.status = status

    def toJSON(self):
        return {"name": self.name, "baudRate": self.baudRate, "serial": self.serial, "port": self.port, "status": self.status}

    def __hash__(self):
        return self.serial

    def __repr__(self):
        return "name: {0} baud rate: {1} serial: {2} port: {3} status: {4}".format(self.name, self.baudRate, self.serial, self.port, self.status)


class SensorManager():

        def add(self, sensor):
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            jsonSensors.append({"name": sensor.name, "baudRate": sensor.baudRate, "serial": sensor.serial, "port": sensor.port, "status": sensor.status})

            config.set('DEFAULT', 'sensors', json.dumps(jsonSensors, indent=4))
            config.write(open("config.ini", "w"))

        def remove(self, sensor):
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            newSensorJson = []
            for jsonSensor in jsonSensors:
                if(jsonSensor["serial"] != sensor.serial):
                    newSensorJson.append(jsonSensor)

            config.set('DEFAULT', 'sensors', json.dumps(newSensorJson, indent=4))
            config.write(open("config.ini", "w"))


        def update(self, sensor):
            print("updating being called")
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            for jsonSensor in jsonSensors:
                if(jsonSensor["serial"] == sensor.serial):
                    jsonSensor["name"] = sensor.name
                    jsonSensor["baudRate"] = sensor.baudRate
                    jsonSensor["serial"] = sensor.serial
                    jsonSensor["port"] = sensor.port
                    jsonSensor["status"] = sensor.status

            config.set('DEFAULT', 'sensors', json.dumps(jsonSensors, indent=4))
            config.write(open("config.ini", "w"))

        def get(self):
            config = configparser.ConfigParser()
            config.read('config.ini')
            jsonSensors = json.loads(config['DEFAULT']['sensors'])

            sensorArray = []

            for jsonSensor in jsonSensors:
                s = Sensor(jsonSensor["name"], jsonSensor["baudRate"], jsonSensor["serial"], jsonSensor["port"], jsonSensor["status"])
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
