import SensorManager as Sm
import serial
from threading import Thread
from pyACS import *
import dataManager as dm

sensorManager = Sm.SensorManager()

class DataCollector():
    def __init__(self):
        self.updateSensors()

    def updateSensors(self):
        self.sensors = sensorManager.get()
        self.flags = {}
        self.serialPorts = {}

        for sensor in self.sensors:

            sensor.status = "off"
            sensorManager.update(sensor)




    def start(self, sensor):
        print("Start Data Collection")
        sensor.status = "on"
        sensorManager.update(sensor)

        self.flags[sensor.serial] = True

        serialPort = serial.Serial()
        serialPort.baudrate = sensor.baudRate # 115200
        serialPort.port = sensor.port # "/dev/cu.usbmodem14101"#
        self.serialPorts[sensor.serial] = serialPort

        try:
            serialPort.open()
        except:
            print("Couldnt open port")

        if(sensor.name == "ACS"):
            thread = Thread(target = self.ACS, kwargs = dict(serialPort=serialPort, sensor=sensor))
            thread.start()
        else:
            print("Sensor not available")




    def startAll(self):
        for sensor in self.sensors:
            self.start(sensor)

    def stop(self, sensor):
        sensor.status = "off"
        sensorManager.update(sensor)
        self.flags[sensor.serial] = False

        serialPort = self.serialPorts[sensor.serial]
        serialPort.close()


        # close port

        # serialPort = self.serialPorts[sensor]
        # thread = self.threads[sensor]

        # terminate tread

    def stopAll(self):
        for sensor in self.sensors:
            self.stop(sensor)

    def ACS(self, serialPort, sensor):
        #file = open(files[i] + "Bytes.txt", "a")
        #decodedFile = open(files[i] + ".txt", "a")
        newACS = acs.ACS("acs301.dev")
        byteString = b""#keeps track of all bytes in current frame
        while(self.flags[sensor.serial]):
            byteString += serialPort.readline()#read incoming bytes
            bitEnd = byteString.find(b'\xff\x00\xff\x00')#checks for beginning of next frame
            if not (bitEnd == -1):
                try:

                    dm.addData(sensor.name + "_bin", byteString.hex(), "bin")
                    dm.addData(sensor.name, str(newACS.unpack_frame(b'\xff\x00\xff\x00' + byteString[0:bitEnd]))+ "\n", "txt")
                    if(dm.status == 1):
                        # thread = Thread(target = dm.sendData, args = {sensorName + "_bin", "bin"})
                        # thread.start()
                        # thread = Thread(target = dm.sendData, args = {sensorName, "txt"})
                        # thread.start()
                        print("Writing Data For: ", str(sensor.serial))
                except:
                    print("something went wrong")
                byteString = byteString[bitEnd + 4:]#deletes old frame
