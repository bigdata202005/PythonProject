import copy
from urllib.request import Request, urlopen
import datetime

import xmltodict

URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"
DATA = {"key": None, "targetDt": None}
print(DATA)
print("*" * 80)
data = copy.copy(DATA)
data["key"] = "430156241533f1d058c603178cc3ca0e"
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
year = yesterday.year;
month = yesterday.month
day = yesterday.day
data["targetDt"] = "{:04d}{:02d}{:02d}".format(year, month, day)
print(data)
print("*" * 80)
URL += "?key={}&targetDt={}".format(data["key"], data["targetDt"])
print(URL)
print("*" * 80)
req = Request(URL, method="GET")
res = urlopen(req)
data = res.read().decode('utf-8')
print(type(data))
print(data)
print("*" * 80)

xml_dict = xmltodict.parse(data)
print(xml_dict)
print("*" * 80)

print(xml_dict["boxOfficeResult"]["boxofficeType"])
print(xml_dict["boxOfficeResult"]["showRange"])
print(xml_dict["boxOfficeResult"]["dailyBoxOfficeList"])
print("*" * 80)
for dailyBoxOffice in xml_dict["boxOfficeResult"]["dailyBoxOfficeList"]["dailyBoxOffice"]:
    # print(type(dailyBoxOffice), dailyBoxOffice)
    print("{:02d}.{}({})".format(int(dailyBoxOffice['rank']), dailyBoxOffice['movieNm'], dailyBoxOffice['openDt']))
print("*" * 80)
