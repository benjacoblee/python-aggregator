import os
import requests
import geocoder
from dotenv import load_dotenv

from feed_path import feed_path

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
g = geocoder.ip('me')
(LATITUDE, LONGITUDE) = g.latlng


class Weather:
    def get_weather(self):
        res = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&APPID={WEATHER_API_KEY}")
        forecast = res.json()['daily'][0]
    # today_weather = forecast['weather'][0]['description']
        return forecast

    def write_weather(self):
        weather = self.get_weather()
        with open(feed_path, "a") as file:
            file.write(f"""
            <h2>Weather Forecast</h2>
                <p>Today's weather: {weather['weather'][0]['description'].capitalize()} 
                    <span style="max-height:inherit">
                        <img src='https://openweathermap.org/img/wn/{weather["weather"][0]["icon"]}.png'/>
                    </span>
                </p>
            """)


# if 'rain' in today_weather:
#     requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage',
#                  params={'chat_id': CHANNEL_NAME,
#                          'text': 'It\'s going to rain today' + u'\U00002614' + ', take your umbrella with you!'})
