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
  if url in news :
    return False
  
  if len(news) >= 500 :
    news.pop(0)

  else :
    news.append(url)  
    requests.patch(
      f"https://api.github.com/gists/{GIST_ID}",
      headers={
         "Authorization": f"Bearer {GIST_TOKEN}"
      },
      json={
        "files": {
          "news.json": {
            "content": json.dumps(news)
          }
        }
      }
    )
    return True
  


def delete_last_news() :
  r = requests.get(
    f"https://api.github.com/gists/{GIST_ID}",
    headers={
      "Authorization": f"Bearer {GIST_TOKEN}"
    }
  )
  data = r.json()
  content = data["files"]["news.json"]["content"]
  news = json.loads(content)
  news.pop()
  requests.patch(
    f"https://api.github.com/gists/{GIST_ID}",
    headers={
       "Authorization": f"Bearer {GIST_TOKEN}"
    },
    json={
      "files": {
        "news.json": {
          "content": json.dumps(news)
        }
      }
    }
  )