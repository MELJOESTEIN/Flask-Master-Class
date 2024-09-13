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
