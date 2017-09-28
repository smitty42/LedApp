from flask import Flask
from serial_dpot import set_value
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Submit an intager between 0 and 255 as a uri.'

@app.route('/<int:wiper_value>')
def get_wiper_value(wiper_value):
        set_value(wiper_value)
        return str(wiper_value)
