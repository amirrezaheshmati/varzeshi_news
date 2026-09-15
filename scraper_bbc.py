import requests
from bs4 import BeautifulSoup


def read_news() :
  response = requests.get(
    "https://www.bbc.com/persian/topics/cz7k02839xet.lite",
    headers={
        "User-Agent": "Mozilla/5.0"
    }
  )
  soup = BeautifulSoup(response.text, "html.parser")
  links = filtered(soup)
  print("links len :" ,len(links))
  for link in links :
    main_link = link.replace(".lite" , "")
    response = requests.get(
      main_link,
      headers={
          "User-Agent": "Mozilla/5.0"
      }
    )
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one("h1").get_text()
    image_url = soup.select_one("figure img")["src"]
    summary = soup.select_one("b").get_text()
    yield {
      "title" : title,
      "image_url" : image_url,
      "summary" : summary,
      "link" : main_link
    }


def filtered(soup) :
  links = []
  for li in soup.find_all("li") :
    a = li.find("a" , href = True)
    if a :
      link = a["href"]
      if "https://www.bbc.com/persian/articles/" in link :
        links.append(link)
  return links