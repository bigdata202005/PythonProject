from urllib.request import Request, urlopen
import json

URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101"
req = Request(URL, method="GET")
res = urlopen(req)
data = res.read().decode('utf-8')
print(type(data))
print(data)
print("*" * 80)

json_data = json.loads(data)
print(type(json_data))
print(json_data)
print("*" * 80)

box_office_list = json_data["boxOfficeResult"]["dailyBoxOfficeList"]
print(box_office_list)

for box_office in box_office_list:
    print("{:02d}위. {}({})".format(int(box_office["rank"]), box_office["movieNm"], box_office["openDt"]))