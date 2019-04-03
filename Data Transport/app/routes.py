from app import app
import os
from flask import request, jsonify
import configparser
import json

@app.route('/send', methods=['POST'])
def send():

    app.logger.info("test")

    sensors = request.json

    for sensor in sensors:
        name = sensor["name"]
        data = sensor["data"]

        try:
            with open(name + ".txt", "a") as file:

                for values in data:
                    file.write(values["value"] + os.linesep)

                file.close()
                app.logger.info("closing: " + name + ".txt")

        except IOError as e:
            app.logger.info("Couldn't open or write to file (%s)." % e)
            abort(500)


    return "{success: true}"

@app.route('/updateSensors', methods=['POST'])
def updateSensors():

    jsonSensors = request.json["sensors"]

    # print(jsonSensors)

    config = configparser.ConfigParser()
    config.set('DEFAULT', 'sensors', json.dumps(jsonSensors, indent=4))
    print(config.write(open("config.ini", "w")))

    return json.dumps({"error": False})



@app.route('/getSensors', methods=['GET'])
def getSensors():

    config = configparser.ConfigParser()
    config.read('config.ini')
    jsonSensors = json.loads(config['DEFAULT']['sensors'])
    return json.dumps({"error": False, "sensors": jsonSensors})
