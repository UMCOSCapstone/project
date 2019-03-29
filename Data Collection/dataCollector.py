import serial
import time
from pyACS import *
import dataManager as dm
from threading import Thread

import socket;

def ACS(sensor):
    connected = False
    while(not connected):
        print("test")
        try:        
            host = socket.gethostname()  # as both code is running on same pc
            port = 5000  # socket server port number

            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            connected = True
        except:
            print("connection failed, trying again in 5 seconds")
            time.sleep(5)
    #file = open(files[i] + "Bytes.txt", "a")
    #decodedFile = open(files[i] + ".txt", "a")
    newACS = acs.ACS("acs301.dev")
    byteString = b""#keeps track of all bytes in current frame
    while(True):
        byteString += sensor.readline()#read incoming bytes
        bitEnd = byteString.find(b'\xff\x00\xff\x00')#checks for beginning of next frame
        if not (bitEnd == -1):
            try:
                #decodedFile.write(str(newACS.unpack_frame(b'\xff\x00\xff\x00' + byteString[0:bitEnd]))+ "\n")
                #file.write(byteString.hex())#writes incoming data to appropriate file
                #dm.sendData(files[i], byteString.hex())
                print("Writing Data")
            
            except:
                print("something went wrong")
            client_socket.send(byteString)
            byteString = byteString[bitEnd + 4:]#deletes old frame

def SensorInput(sensor):
    connected = False
    while(not connected):
        print("test")
        try:        
            host = socket.gethostname()  # as both code is running on same pc
            port = 5000  # socket server port number

            client_socket = socket.socket()  # instantiate
            client_socket.connect((host, port))  # connect to the server
            connected = True
        except:
            print("connection failed, trying again in 5 seconds")
            time.sleep(5)
    while(1):
        print(test)
        client_socket.send(byteString.encode())
        #dm.sendData(files[i], byteString.hex())


config = open("config.text", "r")
ser = []#stores all serial ports
files = []#stores each sensor's file
count = 0#counts how many sensors there are
        
            
sensorType = []


while True:
    lineReader = config.readline()#reads the config file
    if not lineReader:#if the end of the file has been reachd
        break;
    else:
        files.append(lineReader[:-1])#opens/creates a new file for the sensor
        ser.append(serial.Serial())#adds new serial port
        lineReader = config.readline()
        ser[count].baudrate = lineReader[:-1]
        lineReader = config.readline()
        ser[count].port = lineReader[:-1]
        lineReader = config.readline()
        sensorType.append(lineReader)

        try:
            ser[count].open()
        except:
            import serial.tools.list_ports
            print(list(serial.tools.list_ports.comports()))

        print(ser[count].is_open)
        count += 1
for i in range(count):
    if not(sensorType[i].find("ACS") == -1):
        thread = Thread(target = ACS, args = {ser[i]})
        thread.start()
    else:
        thread = Thread(target = SensorInput, args = {ser[i]})
        thread.start()
        
