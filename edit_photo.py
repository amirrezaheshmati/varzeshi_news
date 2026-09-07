from PIL import Image , ImageDraw
import requests
import uuid

LOGO = "logo.png"


def edit_photo(image_url) :
  response = requests.get(image_url)
  print("get image")
  filename = f"{uuid.uuid4()}.png"
  with open (filename , "wb") as file :
    file.write(response.content)
  
  background = Image.open(filename).convert("RGBA")
  logo_image = Image.open(LOGO).convert("RGBA")
  logo_width = int(background.width * 0.15)

  logo_image = logo_image.resize((logo_width , logo_width))

  mask = Image.new("L" , (logo_width , logo_width) , 0)
  draw = ImageDraw.Draw(mask)
  draw.ellipse((0,0,logo_width,logo_width),fill=255)
  logo_image.putalpha(mask)

  background.alpha_composite(logo_image,(background.width - logo_image.width - 20,20))
  background.convert("RGB").save(filename)
  return filename