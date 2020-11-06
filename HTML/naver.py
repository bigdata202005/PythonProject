import requests
from bs4 import BeautifulSoup

url = "https://datalab.naver.com/keyword/realtimeList.naver"
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup.prettify())
realtimeList = soup.find_all("div", {'class': 'ranking_box'})
print(realtimeList)
