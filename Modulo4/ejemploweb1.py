""" import requests
from xml import parsers 
r = requests.get("https://medium.com/@joerosborne/intro-to-web-scraping-build-your-first-scraper-in-5-minutes-1c36b5c4b110")
contenido = r.content

parseado = parsers(contenido)

parseado
print(r.status_code)
 """