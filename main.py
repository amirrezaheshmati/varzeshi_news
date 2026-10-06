import scarper_photo
import bot
import check_exist
import edit_photo
import asyncio
import time




def main() :
  print("start")
  try :
    for new in scarper_photo.read_news() :
      text = ""
      if new :
        if check_exist.check(new["link"]) :
          image_filename = edit_photo.edit_photo(new["image_url"])
          print("image created")
          text += f"<b>{new["title"]}</b>"
          text += "\n" + "\n" + "\n"
          text += f"{new["summary"]}"
          text += "\n" + "\n"
          text += "منبع : ورزش 3" + "\n"
          text += "<b>ورزش نما</b>" + "\n"
          text += "@VarzNema"
          asyncio.run(bot.main(image_filename , text))
          print("new sended")
          time.sleep(60)
  except Exception as e :
    import traceback

    print("ERROR:", repr(e))
    traceback.print_exc()
    raise


# if __name__ == "__main__" :
  # main()