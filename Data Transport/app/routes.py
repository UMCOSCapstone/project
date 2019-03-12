from app import app
import os
from flask import request, jsonify

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
