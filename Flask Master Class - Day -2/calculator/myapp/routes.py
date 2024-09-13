from myapp import app

@app.route('/home')
def index():
    return "<h1>Calculator coming soon!</h1>"