from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config.from_object('config')

# Ensure the instance folder exists
if not os.path.exists('instance'):
    os.makedirs('instance')

# Set up logging
if not app.debug:
    file_handler = RotatingFileHandler('instance/calculator.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Calculator startup')

# Ensure the secret key is set
if not app.secret_key:
    app.secret_key = os.urandom(24)
    app.logger.warning('No secret key set. Using a random one.')

from myapp import routes