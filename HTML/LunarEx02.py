import requests
from bs4 import BeautifulSoup

url = "https://astro.kasi.re.kr/life/pageView/5"
webpage = requests.get(url)
print(str(webpage.content.decode('utf-8')))
print("_" * 80)

soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)
print("_" * 80)

table = soup.table
print(type(table))
print(table)
print("_" * 80)

tbody = soup.tbody
print("tbody")
print(type(tbody))
print(tbody)
print("_" * 80)

tr = soup.tr
print("tr")
print(type(tr))
print(tr)
print("_" * 80)

trs = soup.find_all('tr')
print("trs")
print(type(trs))
print(trs)
print("_" * 80)

print(trs[0])
print(trs[1])
print("_" * 80)
for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(type(td), td.string.strip())
    print('~' * 40)

