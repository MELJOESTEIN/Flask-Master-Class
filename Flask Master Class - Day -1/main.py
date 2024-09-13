from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/name')
def hello(name = "John"):
    return render_template('hello.html', person=name)