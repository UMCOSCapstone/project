from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.run(host='0.0.0.0' , port=5000)

from app import routes
