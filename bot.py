from telegram import Bot
import os

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = "@VarzNema"

async def main(image , text) :
  bot = Bot(token=TOKEN)

  try :
    await bot.send_photo(
      chat_id=CHANNEL_ID,
      photo= image ,
      caption= text,
      read_timeout=120,
      write_timeout=120,
      connect_timeout=90,
      pool_timeout=90,
      parse_mode="HTML"
    )
  except :
    pass
  os.remove(image)