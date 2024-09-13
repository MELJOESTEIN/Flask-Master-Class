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
- [https://machinelearningprojects.net/flask-projects/#google_vignette](https://machinelearningprojects.net/flask-projects/#google_vignette)
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
1. Create a new file called `myapp.py` and open it in your text editor.

2. Add the following code to `myapp.py`:

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
```

### 3. Run the application
1. In your terminal, make sure you're in the project directory and your virtual environment is activated.

2. Run the Flask application:
   ```
   flask --app myapp run --debug
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





# Flask Master Class - Day 2: Flask Fundamentals and Project Setup


This part outlines the topics covered in Day 2 of the Flask Master Class:

* **HTTP Methods and Form Handling:**
    * Introduction to common HTTP methods (GET, POST, PUT, DELETE)
    * Handling form submissions in Flask
    * Using the `request` object to access form data
    * Demonstration: Simple form handling example

   

**Coding Part: Flask Calculator Project Setup**

This section provides instructions for setting up the Flask Calculator project you'll be developing during the class.

**Project Structure**

```
calculator/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│       ├── css/
│       └── js/
│   └── templates/
│       ├── base.html
│       └── calculator.html
├── config.py
├── main.py
└── requirements.txt
```

**Setup Instructions**

1. **Create a project directory:**

   ```bash
   mkdir calculator
   cd calculator
   ```

2. **Set up a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Flask:**

   ```bash
   pip install Flask
   ```

4. **Create the project structure shown above.**

5. **Initialize your Flask app in `app/__init__.py`:**

   ```python
   from flask import Flask

   app = Flask(__name__)

   from app import routes
   ```

6. **Set up a basic route in `app/routes.py`:**

   ```python
   from app import app

   @app.route('/')
   def index():
       return "Calculator coming soon!"
   ```

7. **Run the app using `run.py`:**

   ```python
   from app import app

   if __name__ == '__main__':
       app.run(debug=True)
   ```

8. **Create a `requirements.txt` file to list dependencies:**

   ```bash
   pip freeze > requirements.txt
   ```

9. **Run your Flask app:**

   ```bash
   flask --app myapp run --debug
   ```

Now you have a basic Flask Calculator project ready for further development!

**Practical Exercises**

1. **Create a simple form:** Build a form in Flask that accepts two numbers and an operation (e.g., addition, subtraction), then calculates and displays the result.
2. **Configure your project:** Set up a `config.py` file to manage configuration settings like debug mode and a secret key.
3. **Add static styles:** Create a CSS file in the `static/css` directory and style your calculator form using CSS.
4. **Flask extensions:** Research and implement a Flask extension in your project (e.g., Flask-Bootstrap for easy styling).

**Remember:** Refer to the Flask documentation ([https://flask.palletsprojects.com/en/2.3.x/](https://flask.palletsprojects.com/en/2.3.x/)) for more details and experiment with the code as you learn.



# Flask Master Class - Day 3: Advanced Flask and Calculator Project 

## Overview

This project is an advanced Flask-based web calculator application developed as part of the Flask Master Class - Day 3. It demonstrates the use of advanced Flask concepts and implements a fully functional calculator with error handling, logging, and session management.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Advanced operations (exponentiation, square root)
- Error handling for invalid expressions
- Logging of calculations and errors
- Session management to store the last calculation
- Responsive web interface

## Project Structure

```
calculator/
├── myapp/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   └── templates/
│       ├── base.html
│       └── calculator.html
├── config.py
├── main.py
└── requirements.txt
```

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation


1. Create a virtual environment:
   ```
   python -m venv venv
   ```
   
    On Windows:
    ```
   py -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

The application uses a `config.py` file for configuration. You can modify this file to change application settings such as the secret key and debug mode.

## Running the Application

To run the application, execute:

```
python main.py
```

The application will start, and you can access it by opening a web browser and navigating to `http://localhost:5000`.

## Usage

1. Enter a mathematical expression in the input field.
2. Click the "Calculate" button or press Enter.
3. The result will be displayed below the input field.
4. If there's an error in your expression, an error message will be shown.
5. The last calculation is stored in the session and displayed on the page.

## Code Overview

### `myapp/__init__.py`

This file initializes the Flask application, sets up configuration, logging, and registers routes.

### `myapp/routes.py`

Contains the route definitions for the calculator application. It includes:
- The main calculator route that handles GET and POST requests
- Error handling for invalid expressions
- Logging of calculations and errors
- Session management to store the last calculation

### `myapp/templates/calculator.html`

The HTML template for the calculator interface. It includes:
- A form for entering mathematical expressions
- Display area for the calculation result
- Display of the last calculation from the session

### `myapp/static/css/style.css`

Contains CSS styles for the calculator interface, making it responsive and visually appealing.

### `myapp/static/js/script.js`

Contains JavaScript code for any client-side functionality (if implemented).

### `config.py`

Configuration file for the Flask application. It includes settings like the secret key and debug mode.

### `main.py`

The entry point for running the Flask application.

## Error Handling

The application includes robust error handling:
- Invalid mathematical expressions are caught and appropriate error messages are displayed.
- Internal server errors are logged and a generic error message is shown to the user.

## Logging

The application logs important events:
- Successful calculations
- Errors in calculations
- Application startup and shutdown

Logs are stored in the `instance` folder.

## Session Management

The application uses Flask's session management to store the last calculation. This persists across multiple requests from the same client.

## Contributing

Contributions to improve the calculator are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request




# Flask Master Class - Day 4 : API Integration working with external APIs (Weather API)

This is a simple Flask-based web application that fetches and displays weather data using the Open-Meteo API. It's designed as a learning project for beginners to understand the basics of web development with Python and Flask.

## Project Structure

```
weather_app/
│
├── app.py
├── templates/
│   └── weather.html
└── requirements.txt
```

- `app.py`: This is the main Python file containing the Flask application code.
- `templates/weather.html`: This is the HTML template for the web page.
- `requirements.txt`: This file lists the Python packages required for the project.

## Code Explanation

### app.py

This file contains the main logic of our Flask application. Let's break it down:

1. Importing necessary modules:
   ```python
   from flask import Flask, render_template, request
   import requests
   ```
   - `Flask`: The core Flask module to create our web application.
   - `render_template`: Used to render HTML templates.
   - `request`: Allows us to handle HTTP requests.
   - `requests`: Used to make HTTP requests to the weather API.

2. Creating the Flask application:
   ```python
   app = Flask(__name__)
   ```

3. Defining the route and view function:
   ```python
   @app.route('/', methods=['GET', 'POST'])
   def weather():
       # Function body
   ```
   This sets up the main (and only) route of our application. It handles both GET and POST requests.

4. Handling form submission and API request:
   ```python
   if request.method == 'POST':
       latitude = request.form['latitude']
       longitude = request.form['longitude']
       url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
       
       response = requests.get(url)
       if response.status_code == 200:
           weather_data = response.json()
   ```
   This code runs when the form is submitted. It retrieves the latitude and longitude from the form, constructs the API URL, sends a request to the Open-Meteo API, and stores the response.

5. Rendering the template:
   ```python
   return render_template('weather.html', weather=weather_data)
   ```
   This line renders the `weather.html` template, passing the weather data to it.

### templates/weather.html

This file contains the HTML structure of our web page. Key points:

1. It uses a form to collect latitude and longitude from the user.
2. It uses Jinja2 templating to display the weather data dynamically.
3. It includes conditional rendering to only show weather data when it's available.

## Learning Points

1. **Flask Basics**: This project demonstrates how to set up a basic Flask application with routing and template rendering.

2. **HTTP Methods**: The application handles both GET (initial page load) and POST (form submission) requests.

3. **API Integration**: It shows how to make requests to an external API (Open-Meteo) and handle the response.

4. **HTML Templates**: The project uses Jinja2 templating to dynamically render HTML based on the data received from the server.

5. **Form Handling**: It demonstrates how to create and handle HTML forms in Flask.

6. **JSON Parsing**: The application parses JSON data received from the API.

7. **Error Handling**: Basic error handling is implemented to check if the API request was successful.


   ## Weather API document :  ([https://open-meteo.com/](https://open-meteo.com/)) 

## Next Steps

To further develop this project, consider:

1. Adding error handling and user feedback for invalid inputs.
2. Implementing caching to store recent weather data and reduce API calls.
3. Enhancing the UI with CSS and potentially JavaScript for a better user experience.
4. Adding more weather data points or visualization of the data.

Remember, coding is a journey of continuous learning and improvement. Don't hesitate to experiment with the code and expand its functionality!
