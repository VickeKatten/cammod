from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)
latest = {}

@app.route('/')
def index():
    if not latest:
        return "<h2>No camera data received yet.</h2>"
    return render_template_string("""
        <h1>Camera Feed</h1>
        <p><b>Player:</b> {{player}}</p>
        <p><b>Coordinates:</b> X={{x}}, Y={{y}}, Z={{z}}</p>
        <p><b>Timestamp:</b> {{time}}</p>
    """, **latest)

@app.route('/upload', methods=['POST'])
def upload():
    global latest
    data = request.json
    data["time"] = datetime.now().strftime("%H:%M:%S")
    latest = data
    print("Received camera data:", latest)
    return "OK"
