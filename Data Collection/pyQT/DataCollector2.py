import SensorManager as Sm
import serial
from threading import Thread
from pyACS import *
import time
import dataManager as dm
import socket

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
        elif(sensor.name == "BB3"):
            thread = Thread(target = self.BB3, kwargs = dict(serialPort=serialPort, sensor=sensor))
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

        # connected = False
        # while(not connected):
        #     print("test")
        #     try:
        #         # host = socket.gethostname()  # as both code is running on same pc
        #         # port = 5000  # socket server port number
        #         #
        #         # client_socket = socket.socket()  # instantiate
        #         # client_socket.connect((host, port))  # connect to the server
        #
        #         sio.emit('my event', {'data': 'foobar'})
        #
        #         connected = True
        #     except:
        #         print("connection failed, trying again in 5 seconds")
        #         time.sleep(5)

        #file = open(files[i] + "Bytes.txt", "a")
        #decodedFile = open(files[i] + ".txt", "a")
        newACS = acs.ACS("acs301.dev")
        byteString = b""#keeps track of all bytes in current frame
        while(self.flags[sensor.serial]):
            byteString += serialPort.readline()#read incoming bytes
            bitEnd = byteString.find(b'\xff\x00\xff\x00')#checks for beginning of next frame
            if not (bitEnd == -1):
                try:


                    # print(str(newACS.unpack_frame(b'\xff\x00\xff\x00' + byteString[0:bitEnd]))+ "\n")
                    # dm.addData(sensor.name + "_bin", byteString.hex(), "bin")
                    # print(newACS.unpack_frame(b'\xff\x00\xff\x00' + byteString[0:bitEnd]).c_ref[0])

                    unpacked = newACS.unpack_frame(b'\xff\x00\xff\x00' + byteString[0:bitEnd])

                    jsonData = {"frame_len": unpacked.frame_len, "frame_type": unpacked.frame_type, "serial_number": unpacked.serial_number, "a_ref_dark": unpacked.a_ref_dark, "p": unpacked.p, "a_sig_dark": unpacked.a_sig_dark, "t_ext": unpacked.t_ext, "t_int": unpacked.t_int, "c_ref_dark": unpacked.c_ref_dark, "c_sig_dark": unpacked.c_sig_dark, "time_stamp": unpacked.time_stamp, "output_wavelength": unpacked.output_wavelength, "c_ref": unpacked.c_ref.tolist(), "a_ref": unpacked.a_ref.tolist(), "c_sig": unpacked.c_sig.tolist(), "a_sig": unpacked.a_sig.tolist()}

                    dm.addData(sensor, jsonData, "txt")
                    # if(dm.status == 1):
                        # thread = Thread(target = dm.sendData, args = {sensorName + "_bin", "bin"})
                        # thread.start()
                        # thread = Thread(target = dm.sendData, args = {sensorName, "txt"})
                        # thread.start()
                        # client_socket.send(b'\xff\x00\xff\x00' + byteString[0:bitEnd])
                    print("Writing Data For: ", str(sensor.serial))
                except:
                    print("something went wrong")
                byteString = byteString[bitEnd + 4:]#deletes old frame

    def BB3(self, serialPort, sensor):

        # connected = False
        # while(not connected):
        #     print("test")
        #     try:
        #         # host = socket.gethostname()  # as both code is running on same pc
        #         # port = 5000  # socket server port number
        #         #
        #         # client_socket = socket.socket()  # instantiate
        #         # client_socket.connect((host, port))  # connect to the server
        #
        #         sio.emit('my event', {'data': 'foobar'})
        #
        #         connected = True
        #     except:
        #         print("connection failed, trying again in 5 seconds")
        #         time.sleep(5)

        #file = open(files[i] + "Bytes.txt", "a")
        #decodedFile = open(files[i] + ".txt", "a")
        while(self.flags[sensor.serial]):
            byteString = str(serialPort.readline())[1:-5].split("\\t")[2:]#read incoming bytes
            print(byteString)
            #for i in byteString:
            #    print(i + "test,")
            try:
                # print(str(newACS.unpack_frame(b'\xff\x00\xff\x00' + byteString[0:bitEnd]))+ "\n")
                # dm.addData(sensor.name + "_bin", byteString.hex(), "bin")
                # print(newACS.unpack_frame(b'\xff\x00\xff\x00' + byteString[0:bitEnd]).c_ref[0])
                dm.addData(sensor, byteString, "txt")
                # if(dm.status == 1):
                    # thread = Thread(target = dm.sendData, args = {sensorName + "_bin", "bin"})
                    # thread.start()
                    # thread = Thread(target = dm.sendData, args = {sensorName, "txt"})
                    # thread.start()
                    # client_socket.send(b'\xff\x00\xff\x00' + byteString[0:bitEnd])
                print("Writing Data For: ", str(sensor.serial))
            except:
                print("something went wrong")
