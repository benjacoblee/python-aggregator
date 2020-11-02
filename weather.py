import os
import requests
import geocoder
from dotenv import load_dotenv


load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
g = geocoder.ip('me')
(LATITUDE, LONGITUDE) = g.latlng


def get_weather():
    res = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&APPID={WEATHER_API_KEY}")
    forecast = res.json()['daily'][0]
    # today_weather = forecast['weather'][0]['description']
    return forecast
# if 'rain' in today_weather:
#     requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage',
#                  params={'chat_id': CHANNEL_NAME,
#                          'text': 'It\'s going to rain today' + u'\U00002614' + ', take your umbrella with you!'})


get_weather()
