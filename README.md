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
```

Run the application:
```
flask --app main run ( without debug mode off ) 
```
```
flask --app main run --debug ( with debug mode on )
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

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
```

**Flask Templates with Jinja2**

This part explains how to structure and use templates in your Flask applications.

**Template Folder Location:**

- For standalone modules (`.py` files), Flask searches for templates in a folder named `templates` located at the same level as the module.
- For packages, the `templates` folder resides within the package directory, alongside the `__init__.py` file.

**Example Structure:**

**Case 1: Module**

```
main.py
templates/
    hello.html
```

**Case 2: Package**

```
application/
    __init__.py
    templates/
        hello.html
```

**Jinja2 Templating Language**

Flask leverages Jinja2 for powerful templating capabilities. Jinja2 allows you to combine static content with dynamic data from your Python code. For comprehensive guidance, refer to the official Jinja2 documentation: [https://jinja.palletsprojects.com/templates/](https://jinja.palletsprojects.com/templates/)

**Example Template:**

```html
<!DOCTYPE html>
<title>Hello from Flask</title>

{% if person %}
  <h1>Hello {{ person }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

**Explanation:**

- `<!DOCTYPE html>` declares the document type as HTML.
- `<title>` sets the page title.
- `{% if person %}` starts an if statement.
    - If a variable named `person` is passed to the template with a value, the `<h1>` element displays "Hello [person's name]!"
- `{% else %}` defines the "else" block.
    - If `person` is not provided, the `<h1>` element displays "Hello, World!"
- `{% endif %}` ends the if statement.
- `{{ person }}` interpolates the value of the `person` variable within the `<h1>` element.

**Remember:**

- To pass data from your Flask routes to the template, use the `render_template` function (`from flask import render_template`).
- Jinja2 provides various features like loops, filters, and more for complex templating scenarios.

**Additional Tips**

- Consider organizing templates into subfolders within the `templates` directory for larger projects.
- Maintain code readability by using clear variable names.
- Explore Jinja2's advanced features for richer templating possibilities.




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
