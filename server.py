from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def index():
    x = "Test1"
    y = "Test2"
    return jsonify(a=x,z=y)
