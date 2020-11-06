import requests
from bs4 import BeautifulSoup
import json

url = "https://astro.kasi.re.kr/life/pageView/5"
webpage = requests.get(url)
print(str(webpage.content.decode('utf-8')))
print("_" * 80)

soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)
print("_" * 80)

table = soup.table
tbody = table.tbody
trs = tbody.find_all('tr')
lunar_list = list()
for tr in trs:
    tds = tr.find_all('td')
    lunar_dict = dict()
    lunar_dict['solar'] = tds[0].string.strip()
    lunar_dict['lunar'] = tds[1].string.strip()
    lunar_dict['ganji'] = tds[2].string.strip()
    print(lunar_dict)
    lunar_list.append(lunar_dict)
    print('~' * 40)

print("개수 :", len(lunar_list))
print(lunar_list)

# json저장
with open('lunar.json', 'w', encoding='utf-8-sig') as make_file:
    json.dump(lunar_list, make_file, indent="\t", ensure_ascii=False)

# 저장한 파일 출력하기
with open('lunar.json', 'r', encoding='utf-8-sig') as f:
    json_data = json.load(f)
print(json.dumps(json_data, indent="\t", ensure_ascii=False))

# xml저장



