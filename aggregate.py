import urllib
import os
import requests
import datetime
import subprocess

import praw
import pprint

import feedparser

from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

print(client_id)


reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, grant_type_access='client_credentials',
                     user_agent='script/1.0')


# class Reddit:
#     def ReturnMyFeed(self):
#         myfeed = [submission for submission in reddit.subreddi]
#         for submission in reddit.subreddit("rollerblading+python+frontend+reactjs+webdev").top("week"):

#             title, score, url = submission.title, submission.score, submission.url

#             print(
#                 f"Posted in {submission.subreddit}: {title} - {score} upvotes")


class Reddit:
    def Top(self):
        my_feed = [{"subreddit": submission.subreddit.display_name, "title": submission.title, "score": submission.score, "url": submission.url} for submission in reddit.subreddit(
            "rollerblading+python+frontend+reactjs+webdev").top("day", limit=25)]

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
    <h1> Your feed </h1>
    <h2>Reddit Feed</h2>
    <ul>
    """)

r = Reddit()

for post in r.Top():
    with open("feed.html", "a") as file:
        file.write(f"""
        <a href="{post["url"]}"><li>Posted in r/{post["subreddit"]}: {post["title"]} - {post["score"]} upvotes</li></a>
        """)

with open("feed.html", "a") as file:
    file.write("""</ul>
    <h2>CNA</h2>
    """)

cna = CNA()

with open("feed.html", "a") as file:
    file.write("<h4>Latest News</h4>")

for entry in cna.latest_news():
    with open("feed.html", "a") as file:
        file.write(f"""
        <div class="card mb-2">
        <div class="card-body">
        <a href="{entry["id"]}">{entry["title"]}</a>
        <p>{entry["summary"]}</p>
        </div>
        </div>
        """)

with open("feed.html", "a") as file:
    file.write("<h4>Local News</h4>")

for entry in cna.local_news():
    with open("feed.html", "a") as file:
        file.write(f"""
        <div class="card mb-2">
        <div class="card-body">
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
