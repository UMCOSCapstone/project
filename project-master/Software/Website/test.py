import serial
config = open("config.text", "r")
ser = []#stores all serial ports
files = []#stores each sensor's file
count = 0#counts how many sensors there are

while True:
    lineReader = config.readline()#reads the config file
    if not lineReader:#if the end of the file has been reachd
        break;
    else:
        files.append(open(lineReader[:-1]+".txt", "a"))#opens/creates a new file for the sensor
        ser.append(serial.Serial())#adds new serial port
        lineReader = config.readline()
        ser[count].baudrate = lineReader[:-1]
        lineReader = config.readline()
        ser[count].port = lineReader[:-1]
        try:
            ser.open()
        except:
            print("blah")

        print(ser[count].is_open)
        count += 1



while True:
    for i in range(count):
        files[i].write(ser[i].readline())#writes incoming data to appropriate file
