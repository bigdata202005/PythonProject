from urllib.request import Request, urlopen
import json

URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key=430156241533f1d058c603178cc3ca0e&itemPerPage=100"
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

count = json_data["peopleListResult"]["totCnt"]
print("총인원 :", count)
total_page = (count-1)//100 + 1
print("전체 페이지 :", total_page)
#peopleList = json_data["peopleListResult"]["peopleList"]
#for people in peopleList:
#    print("이름 :", people["peopleNm"])

for page in range(1, total_page+1):
    url2 = URL + "&curPage=" + str(page)
    req = Request(URL, method="GET")
    res = urlopen(req)
    data = res.read().decode('utf-8')
    json_data = json.loads(data)
    print("현재 페이지 :", page)
    peopleList = json_data["peopleListResult"]["peopleList"]
    for people in peopleList:
        print("이름 :", people["peopleNm"])