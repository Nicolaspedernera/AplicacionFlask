from flask import Flask, render_template,request
import requests
import json

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        city = request.form['city']
        country = request.form['country']
        api_key = "24975502a020fb484a527f29ccf30118"

        weather_url = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=metric")

        weather_data = weather_url.json()

        if weather_data["cod"] == "404" :
            return render_template("index.html")
        
        city=weather_data["name"]
        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        iconweather=weather_data["weather"][0]["icon"]
        country=weather_data['sys']['country']
    

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city, country=country, iconweather=iconweather)
    

    return render_template("index.html")

if __name__ =="__main__":

    app.run(host="0.0.0.0", port=4000,debug=True)