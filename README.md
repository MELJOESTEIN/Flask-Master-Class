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
