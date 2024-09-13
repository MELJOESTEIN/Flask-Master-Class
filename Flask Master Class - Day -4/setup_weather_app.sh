#!/bin/bash

# Create project directory
mkdir -p weather_app/templates

# Create and populate app.py
cat << EOF > weather_app/app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()

    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
EOF

# Create and populate weather.html template
cat << EOF > weather_app/templates/weather.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
</head>
<body>
    <h1>Weather App</h1>
    <form method="POST">
        <input type="text" name="latitude" placeholder="Enter latitude" required>
        <input type="text" name="longitude" placeholder="Enter longitude" required>
        <input type="submit" value="Get Weather">
    </form>

    {% if weather %}
        <h2>Current Weather</h2>
        <p>Temperature: {{ weather.current.temperature_2m }}°C</p>
        <p>Wind Speed: {{ weather.current.wind_speed_10m }} m/s</p>

        <h2>Hourly Forecast (Next 24 hours)</h2>
        <table border="1">
            <tr>
                <th>Time</th>
                <th>Temperature (°C)</th>
                <th>Relative Humidity (%)</th>
                <th>Wind Speed (m/s)</th>
            </tr>
            {% for i in range(24) %}
                <tr>
                    <td>{{ weather.hourly.time[i] }}</td>
                    <td>{{ weather.hourly.temperature_2m[i] }}</td>
                    <td>{{ weather.hourly.relative_humidity_2m[i] }}</td>
                    <td>{{ weather.hourly.wind_speed_10m[i] }}</td>
                </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
EOF

# Create requirements.txt
cat << EOF > weather_app/requirements.txt
Flask==2.0.1
requests==2.26.0
EOF

echo "Weather App project created successfully!"
echo ""
echo "To run the application:"
echo "1. Navigate to the weather_app directory:"
echo "   cd weather_app"
echo "2. Create and activate a virtual environment:"
echo "   python -m venv venv"
echo "   source venv/bin/activate  # On Windows, use \`venv\\Scripts\\activate\`"
echo "3. Install the required packages:"
echo "   pip install -r requirements.txt"
echo "4. Run the application:"
echo "   python app.py"
echo ""
echo "The app will be accessible at http://127.0.0.1:5000/"
echo "Use latitude and longitude values to get weather information."
echo "For example: Latitude 52.52, Longitude 13.41 for Berlin, Germany"
