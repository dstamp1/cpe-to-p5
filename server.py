from flask import Flask, render_template, jsonify
import serial  # pyserial




dev_serial = serial.Serial('/dev/tty.usbmodem1301', 115200)

app = Flask(__name__)


@app.route('/')
def index():
    accel_values = [float(s) for s in dev_serial.readline().split()]
    return jsonify(accel_values)



app.run(host='0.0.0.0', debug=True)
