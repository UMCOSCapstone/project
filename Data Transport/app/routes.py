from app import app
import os
import json
from flask import request, jsonify

def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

@static_var("fileOpen", False)
@app.route('/send', methods=['POST'])
def send():

    app.logger.info("test")

    request.json

    name = request.json["name"]
    dataType = request.json["dataType"]
    serialNumber = request.json["serialNumber"]
    records = request.json["data"]

    for record in records:
        try:
            with open(name + "." + dataType, "a") as file:

                file.write(record["value"] + os.linesep)
                file.close()

        except IOError as e:
            abort(500)

    path = "/Users/jacob/Documents/CapstoneProject/project/Data Visualization/Program/my-app/src/"

    while(send.fileOpen):
        print("waiting")
    send.fileOpen = True

    if(os.path.isfile(path + name + ".json")):
        print("file exists")


        jsonReadFile = open(path + name + ".json", "r")

        jsonData = json.load(jsonReadFile)

        for record in records:
            jsonData["data"].append(record)

        jsonFile = open(name + ".json", "w")
        jsonFile.write(json.dumps(jsonData))
        jsonFile.close()

        send.fileOpen = False

    else:
        print("file !exists")
        open(path + name + ".json", "w").write(json.dumps(request.json))
        send.fileOpen = False


    return "{success: true}"
