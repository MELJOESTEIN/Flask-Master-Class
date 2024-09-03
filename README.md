# Flask Master Class - Day 1

## Setting Up the Development Environment

### Python Installation
- Ensure Python 3.x is installed (preferably 3.7+)
- Check version: `python --version`

### Virtual Environments
- Create a virtual environment:
  ```
  python -m venv flask_env
  ```
- Activate the environment:
  - Windows: `flask_env\Scripts\activate`
  - macOS/Linux: `source flask_env/bin/activate`
- Deactivate: `deactivate`

## Installing Flask
```
pip install Flask
```

Verify the installation:
```python
import flask
print(flask.__version__)
```

## Your First Flask Application

Basic structure of a Flask app:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

Run the application:
```
python app.py
```

Access the application in a web browser: `http://127.0.0.1:5000/`

## Understanding Routes and Views

Example of multiple routes:
```python
@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'
```

Dynamic routes:
```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'
```

## Templates and Jinja2 Basics

Basic Jinja2 syntax:
- Variables: `{{ variable_name }}`
- Control structures:
  ```
  {% if condition %}
    ...
  {% endif %}

  {% for item in items %}
    ...
  {% endfor %}
  ```

Rendering templates:
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

## Hands-on Exercise

1. Create a "Hello, World!" Flask application
2. Add a route that displays the current date and time

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)



# Flask Master Class - Day 1 Hands-on Exercise

## Objective
Create a simple Flask application that displays "Hello, World!" and shows the current date and time.

## Prerequisites
- Python 3.x installed
- Flask installed in your virtual environment

## Steps

### 1. Set up the project
1. Create a new directory for your project:
   ```
   mkdir flask_day1_exercise
   cd flask_day1_exercise
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install Flask:
   ```
   pip install Flask
   ```

### 2. Create the Flask application
1. Create a new file called `app.py` and open it in your text editor.

2. Add the following code to `app.py`:

```python
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

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Run the application
1. In your terminal, make sure you're in the project directory and your virtual environment is activated.

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open your web browser and visit:
   - `http://127.0.0.1:5000/` to see the "Hello, World!" message
   - `http://127.0.0.1:5000/time` to see the current date and time

### 4. Experiment and expand
Try adding more routes or modifying the existing ones. For example:
- Add a route that greets a user by name (e.g., `/greet/<name>`)
- Modify the time route to display the time in a different format
- Create a route that returns a random number or a joke

## Conclusion
Congratulations! You've created your first Flask application. This exercise demonstrates the basics of routing and handling requests in Flask.
