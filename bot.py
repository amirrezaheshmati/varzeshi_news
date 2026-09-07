from telegram import Bot
import os

# TOKEN = os.getenv("bot_token")
TOKEN = "8959859464:AAFmiCNHuCiY8kZ-2aCCBQWef7l6F0fUErk"
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