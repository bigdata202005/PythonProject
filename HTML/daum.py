import requests
from bs4 import BeautifulSoup
import json

url = "https://www.daum.net/"
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")
weather = soup.find_all("ul")
for w in weather:
    if w['class'][0] == 'list_weather':
        # print(w)
        for li in w.find_all("li"):
            print(li.find_all('span')[1].string)
            print(li.strong.string)
            print(li.em.string)
            print("~" * 30)

print("_" * 80)
# 이렇게 하면 더 편리하다.
weather = soup.find("ul", {'class':'list_weather'})
# print(weather)
for li in weather.find_all("li"):
    print(li.find_all('span')[1].string)
    print(li.strong.string)
    print(li.em.string)
    print("~" * 30)
