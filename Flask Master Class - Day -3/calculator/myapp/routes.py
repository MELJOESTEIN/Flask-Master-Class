from flask import render_template, request, jsonify, session
from myapp import app
from myapp.forms import CalculatorForm
from myapp.calculator import safe_eval

@app.route('/', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    result = None
    last_calculation = session.get('last_calculation', 'No previous calculation')
    
    if form.validate_on_submit():
        expression = form.expression.data
        app.logger.info(f"Calculating expression: {expression}")
        try:
            result = safe_eval(expression)
            app.logger.info(f"Calculation result: {result}")
            session['last_calculation'] = f"{expression} = {result}"
        except ValueError as e:
            error_message = f"Error: {str(e)}"
            app.logger.error(f"Calculation error: {error_message}")
            result = error_message
    
    return render_template('calculator.html', form=form, result=result, last_calculation=last_calculation)

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    data = request.get_json()
    expression = data.get('expression')
    app.logger.info(f"API calculation request: {expression}")
    try:
        result = safe_eval(expression)
        app.logger.info(f"API calculation result: {result}")
        session['last_calculation'] = f"{expression} = {result}"
        return jsonify({'result': result, 'last_calculation': session['last_calculation']})
    except ValueError as e:
        error_message = f"Error: {str(e)}"
        app.logger.error(f"API calculation error: {error_message}")
        return jsonify({'error': error_message}), 400

@app.errorhandler(404)
def not_found_error(error):
    app.logger.error('404 error occurred')
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error('500 error occurred', exc_info=True)
    return render_template('500.html'), 500