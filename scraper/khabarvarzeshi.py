import feedparser
import requests
from bs4 import BeautifulSoup

RSS_URL = "https://www.khabarvarzeshi.com/rss"


def read_news() :
  feed = feedparser.parse(RSS_URL)
  for news in feed.entries:
    news_list = []
    title = news.get("title", "بدون عنوان")
    link = news.get("link", "بدون لینک")
    summary = news.get("summary", "بدون خلاصه")

    tags = [
      tag.get("term", "")
      for tag in news.get("tags", [])
    ]
    
    if any("فوتبال" in tag for tag in tags) :
      response = requests.get(
        link,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
      )

      soup = BeautifulSoup(response.text, "html.parser")
      content = soup.select_one(".item-text")
      image = soup.select_one("figure.item-img img")
      text = ""
      image_url = ""

      if content :
        text = content.get_text(" " , strip=True)
      if image:
        image_url = image.get("src")

      news_list.append({
        "title" : title,
        "summary" : summary,
        "text" : text,
        "image" : image_url,
        "link" : link
      })
  
  return news_list