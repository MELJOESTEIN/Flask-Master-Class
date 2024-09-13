from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    expression = StringField('Expression', validators=[DataRequired()])
    submit = SubmitField('Calculate')