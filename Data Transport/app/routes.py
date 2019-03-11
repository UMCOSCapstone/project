from app import app
import os
from flask import request, jsonify

@app.route('/send', methods=['POST'])
def send():

#   getting the json data
    sensors = request.json

#   parsing the json data
    for sensor in sensors:
        name = sensor["name"]
        data = sensor["data"]

#       writing the json data to the file
        try:
            with open(name + ".txt", "a") as file:

                for values in data:
                    file.write(values["value"] + os.linesep)

                file.close()
                app.logger.info("closing: " + name + ".txt")

        except IOError as e:
#           error writnig data to file
            app.logger.info("Couldn't open or write to file (%s)." % e)
#           returns 500 error if cannot write data
            abort(500)


    return "{success: true}"
