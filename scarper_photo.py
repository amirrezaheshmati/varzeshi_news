import requests
from bs4 import BeautifulSoup


def read_news() :
  response = requests.get(
    "https://www.varzesh3.com/",
    headers={
        "User-Agent": "Mozilla/5.0"
    }
  )
  soup = BeautifulSoup(response.text, "html.parser")
  links = filtered(soup)
  print("links len :" ,len(links))
  for link in links :
    response = requests.get(
      link,
      headers={
          "User-Agent": "Mozilla/5.0"
      }
    )
    soup = BeautifulSoup(response.text, "html.parser")
    h1 = soup.select_one("h1")
    title = h1.get_text()
    parent = h1.parent
    summary_div = parent.find_all("div")[1]
    summary = summary_div.get_text()
    image_url = parent.parent.select_one("img")["src"]
    yield {
      "title" : title,
      "image_url" : image_url,
      "summary" : summary,
      "link" : link
    }


def filtered(soup) :
  links = []
  div = soup.find("div" , attrs = {"class" : "v3dj266r"})
  for a in div.find_all("a") :
    if a :
      link = a["href"]
      if "https://www.varzesh3.com/news" in link :
        links.append(link)
  return links