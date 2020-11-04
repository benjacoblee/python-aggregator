import feedparser

from feed_path import feed_path


class CNA:
    card_style = "position:relative;display:flex;flex-direction:column;background-color:#fff;background-clip:border-box;border:1px solid rgba(0,0,0,.125); border-radius:.25rem; margin-bottom:1rem;"

    card_body = "display:flex;flex-direction:row;justify-content:space-between;max-width:100%;flex:1 1 auto;min-height:1px;padding:1.25rem"

    card_img_container = "max-width:50%"

    def news(self, type):
        if type == "Latest":
            newsfeed = feedparser.parse(
                "https://www.channelnewsasia.com/rssfeeds/8395986").entries[0:5]
        elif type == "Local":
            newsfeed = feedparser.parse(
                "https://www.channelnewsasia.com/rssfeeds/8396082").entries[0:5]
        return newsfeed

    def iterate_over_news(self, entry):
        with open(feed_path, "a") as file:
            file.write(f"""
                    <div style="{self.card_style}">
                        <div style="{self.card_body}">
                            <div style="{self.card_img_container}">
                                <img style="max-width:80%" src={entry["media_thumbnail"][0]["url"]}/>
                            </div>
                            <div> 
                                <a style="font-size:0.8rem" href="{entry["id"]}">{entry["title"]}</a>
                            </div>
                        </div>
                    </div>
                    """)

    def write_news(self, type):
        with open(feed_path, "a") as file:
            file.write(f"<h3>{type} News</h3>")
        if type == "Latest":
            for entry in self.news(type):
                self.iterate_over_news(entry)
        elif type == "Local":
            for entry in self.news(type):
                self.iterate_over_news(entry)
