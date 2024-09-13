from flask import Blueprint

bp = Blueprint('calculator', __name__)

from myapp.calculator import routes