from dateutil.parser import parse as dtparse
import datetime
from datetime import datetime as dt


from Weather import Weather
from Events import Events
from Reddit import Reddit
from CNA import CNA
from Medium import Medium

from feed_path import feed_path

today = datetime.date.today()

with open(feed_path, "w") as file:
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

w = Weather()
w.write_weather()

e = Events()
e.write_events()

r = Reddit()

with open(feed_path, "a") as file:
    file.write("<h2>Reddit</h2>")


r.fetch_subs_and_write("reactjs")
r.fetch_subs_and_write("webdev")
r.fetch_subs_and_write("frontend")
r.fetch_subs_and_write("python")
r.fetch_subs_and_write("rollerblading")


with open(feed_path, "a") as file:
    file.write("<h2>CNA</h2>")

cna = CNA()

cna.write_news("Latest")
cna.write_news("Local")

# medium = Medium()

with open(feed_path, "a") as file:
    file.write(f"""
            </div>
        </body>
    </html>
    """)
