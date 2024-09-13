from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def current_time():
    now = datetime.now()
    return f'The current date and time is: {now.strftime("%Y-%m-%d %H:%M:%S")}'