from telegram import Bot
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@varzeshi_news_ai"

async def main(image , text) :
  bot = Bot(token=TOKEN)

  await bot.send_photo(
    chat_id=CHANNEL_ID,
    photo= image ,
    caption= text
  )