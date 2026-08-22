from scraper import khabarvarzeshi
from tel import bot
import asyncio

def main() :
  news = khabarvarzeshi.read_news()
  for new in news :
    text = ""
    text += new["title"]
    text += "\n" + "\n"
    text += new["summary"]
    text += "\n" + "\n"
    text += new["link"]
    asyncio.run(bot.main(new["image"] , text))
