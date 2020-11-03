import datetime
from dateutil.parser import parse as dtparse
from datetime import datetime as dt

import weather
import events

from Reddit import Reddit
from CNA import CNA
from Medium import Medium

today = datetime.date.today()
latitude = weather.LATITUDE
longitude = weather.LONGITUDE
weather = weather.get_weather()
events = events.get_events()

with open("feed.html", "w") as file:
    file.write(f"""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
        <body>
            <div class="container mb-5">
            <h1>Your feed for {today.strftime('%d %b %Y')}</h1>
    """)

with open("feed.html", "a") as file:
    file.write(f"""
    <h2>Weather Forecast</h2>
        <p>Today's weather: {weather['weather'][0]['description'].capitalize()} 
            <span style="max-height:inherit">
                <img src='https://openweathermap.org/img/wn/{weather["weather"][0]["icon"]}.png'/>
            </span>
        </p>
    <h2>Upcoming Events</h2>
        <ul>
    """)

for event in events:
    tmfmt = '%d %b %H:%M %p'
    start = event['start'].get('dateTime', event['start'].get('date'))
    date = dt.strftime(dtparse(start), format=tmfmt)
    with open("feed.html", "a") as file:
        file.write(f"""
        <li>{event['summary']} {date}</li>
        """)

with open("feed.html", "a") as file:
    file.write("""
    </ul>
    <h2>Reddit</h2>
    """)

r = Reddit()


r.fetch_subs_and_write("reactjs")
r.fetch_subs_and_write("webdev")
r.fetch_subs_and_write("frontend")
r.fetch_subs_and_write("python")
r.fetch_subs_and_write("rollerblading")


with open("feed.html", "a") as file:
    file.write("<h2>CNA</h2>")

cna = CNA()

cna.write_news("Latest")
cna.write_news("Local")

medium = Medium()

with open("feed.html", "a") as file:
    file.write(f"""
            </div>
        </body>
    </html>
    """)
