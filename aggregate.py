import os
import datetime
import praw
import feedparser
import os
from dotenv import load_dotenv

import weather

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, grant_type_access='client_credentials',
                     user_agent='script/1.0')


class Reddit:
    def Top(self, subreddit):
        my_feed = [{"subreddit": submission.subreddit.display_name, "title": submission.title, "score": submission.score,
                    "url": submission.url} for submission in reddit.subreddit(subreddit).top("day", limit=5)]

        return sorted(my_feed, key=lambda x: x["subreddit"])


class CNA:
    def latest_news(self):
        newsfeed = feedparser.parse(
            "https://www.channelnewsasia.com/rssfeeds/8395986").entries[0:5]

        return newsfeed

    def local_news(self):
        newsfeed = feedparser.parse(
            "https://www.channelnewsasia.com/rssfeeds/8396082").entries[0:5]

        return newsfeed


class Medium:
    def medium_programming(self):
        feed = feedparser.parse(
            "https://medium.com/feed/tag/programming").entries
        return feed

    def medium_python(self):
        feed = feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        ).entries


latitude = weather.LATITUDE
longitude = weather.LONGITUDE
weather = weather.get_weather()


with open("feed.html", "w") as file:
    file.write(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    </head>
    <body>
    <div class="container mb-5">
    <h1>Your feed</h1>
    """)

with open("feed.html", "a") as file:
    file.write(f"""
    <h2>Weather Forecast</h2>
    <p>Today's weather: {weather['weather'][0]['description'].capitalize()}</p>
    <h2>Reddit</h2>
    
    """)

r = Reddit()


def fetch_subs_and_write(sub):
    with open("feed.html", "a") as file:
        file.write(f"""
        <h3>Posts from r/{sub}</h3>
            <ul>
        """)
    for post in r.Top(sub):
        with open("feed.html", "a") as file:
            file.write(f"""
            <a href="{post["url"]}"><li>{post["title"]} - {post["score"]} upvotes</li></a>
            """)
    with open("feed.html", "a") as file:
        file.write("</ul>")


fetch_subs_and_write("reactjs")
fetch_subs_and_write("webdev")
fetch_subs_and_write("frontend")
fetch_subs_and_write("python")
fetch_subs_and_write("rollerblading")


with open("feed.html", "a") as file:
    file.write("<h2>CNA</h2>")

cna = CNA()

card_style = "position:relative;display:flex;flex-direction:column;background-color:#fff;background-clip:border-box;border:1px solid rgba(0,0,0,.125); border-radius:.25rem; margin-bottom:1rem;"

card_body = "flex:1 1 auto;min-height:1px;padding:1.25rem"

with open("feed.html", "a") as file:
    file.write("<h3>Latest News</h3>")

for entry in cna.latest_news():
    with open("feed.html", "a") as file:
        file.write(f"""
        <div style="{card_style}">
        <div style="{card_body}">
        <a href="{entry["id"]}">{entry["title"]}</a>
        <p>{entry["summary"]}</p>
        </div>
        </div>
        """)

with open("feed.html", "a") as file:
    file.write("<h3>Local News</h3>")

for entry in cna.local_news():
    with open("feed.html", "a") as file:
        file.write(f"""
        <div style="{card_style}">
        <div style="{card_body}">
        <a href="{entry["id"]}">{entry["title"]}</a>
        <p>{entry["summary"]}</p>
        </div>
        </div>
        """)

medium = Medium()

with open("feed.html", "a") as file:
    file.write(f"""
    </div>
    </body>
    </html>
    """)
