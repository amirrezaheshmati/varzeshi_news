import requests
import json
import os


GIST_TOKEN = os.environ["GIST_TOKEN"]
GIST_ID = "179ddb3b89fc161ee3ebee5aeb999965"

def check(url) :
  r = requests.get(
    f"https://api.github.com/gists/{GIST_ID}",
    headers={
      "Authorization": f"Bearer {GIST_TOKEN}"
    }
  )
  data = r.json()
  content = data["files"]["news.json"]["content"]
  news = json.loads(content)
  print(news)
  # with open("urls.json" , "r") as file :
    # urls = json.load(file)
  # 
  # if url in urls :
    # return False
  # 
  # if len(urls) >= 500 :
    # urls.pop(0)
# 
  # else :
    # urls.append(url)
    # with open("urls.json" , "w") as file :
      # json.dump(urls , file)  
    # return True
#