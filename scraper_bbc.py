import feedparser
import requests
from bs4 import BeautifulSoup

RSS_URL = "http://newsrss.bbc.co.uk/rss/sportonline_uk_edition/football/rss.xml"

def read_news() :
  try :
    feed = feedparser.parse(RSS_URL)
    print("read_feed , count news:" , len(feed.entries))
    for news in feed.entries:
      title = news.get("title", "بدون عنوان")
      link = news.get("link", "بدون لینک")
      summary = news.get("summary", "بدون خلاصه")

      response = requests.get(
        link,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
      )

      soup = BeautifulSoup(response.text, "html.parser")
      image = soup.select_one("picture img")
      image_url = ""

      if image:
        image_url = image.get("src")

      yield {
        "title" : title,
        "summary" : summary,
        "image_url" : image_url,
        "link" : link
      }
      
  except :
    yield None

read_news()