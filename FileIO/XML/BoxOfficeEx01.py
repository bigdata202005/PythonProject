from urllib.request import Request, urlopen
import json

import xmltodict

URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101"
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
