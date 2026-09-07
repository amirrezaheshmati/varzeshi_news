import json

def check(url) :
  with open("urls.json" , "r") as file :
    urls = json.load(file)
  
  if url in urls :
    return False
  
  if len(urls) >= 500 :
    urls.pop(0)

  else :
    urls.append(url)
    with open("urls.json" , "w") as file :
      json.dump(urls , file)  
    return True
