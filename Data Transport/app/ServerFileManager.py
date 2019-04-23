import configparser
import os
import datetime

class ServerFileManager():

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.fileDirectory = config['DEFAULT']['fileDirectory']

    def addData(self, sensor, data):

        date = datetime.datetime.now()

        print(data.dateTime)

        currentDirectory = self.fileDirectory + str(date.year) + "_" + str(date.month) + "_" + str(date.day) + "_" + str(date.hour) + "00"

        if(not os.path.isdir(currentDirectory)):
            try:
                os.mkdir(currentDirectory, 0o775)

            except:
                print("Cannot make directory")

        file = currentDirectory + "/" + sensor.name + "_" + str(sensor.serial) + ".txt"

        f = open(file, "a")
        f.write(data)
