import os
import praw

from feed_path import feed_path

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, grant_type_access='client_credentials',
                     user_agent='script/1.0')


class Reddit:
    def Top(self, subreddit):
        my_feed = [{"subreddit": submission.subreddit.display_name, "title": submission.title, "score": submission.score,
                    "url": submission.url} for submission in reddit.subreddit(subreddit).top("day", limit=5)]

        return my_feed

    def fetch_subs_and_write(self, sub):
        with open(feed_path, "a") as file:
            file.write(f"""
            <h3>Posts from r/{sub}</h3>
                <ul>
            """)
        for post in self.Top(sub):
            with open(feed_path, "a") as file:
                file.write(f"""
                <a href="{post["url"]}">
                    <li>{post["title"]} - {post["score"]} upvotes</li>
                </a>
                """)
        with open(feed_path, "a") as file:
            file.write("</ul>")
