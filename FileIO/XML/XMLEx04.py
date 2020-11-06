# 외장모듈인 xmltodict를 이용하는 방법
# !pip install xmltodict # 미설치된 경우 설치한다
import json
import xmltodict
# XML파일을 String으로 모두 읽기
file = open('data2.xml', "r")
allLines = file.read()
print(allLines)
print("*" * 80)
# String을 dict로 파싱. 결과가  OrderedDict타입이다.
xml_dict = xmltodict.parse(allLines)
print(xml_dict)
print("*" * 80)
# OrderedDict타입에서 데이터 읽기
print(xml_dict["data"]["@version"])
print(xml_dict["data"]["@size"])
print("*" * 80)

for country in xml_dict["data"]["country"]:
    print("name : {}".format(country["@name"]))
    print("rank : {}".format(country["rank"]))
    print("year : {}".format(country["year"]))
    print("gdppc : {}".format(country["gdppc"]))
    print("neighbor : {}".format(country["neighbor"]))
    if type(country["neighbor"]) == list:
        for neighbor in country["neighbor"]:
            print("neighbor : {}, {}".format(neighbor["@name"], neighbor["@direction"]))
    else:
        print("neighbor : {}, {}".format(country["neighbor"]["@name"], country["neighbor"]["@direction"]))
    print("-" * 80)
print("*" * 80)
# XML을 JSON으로 변환
xml_dict2 = json.loads(json.dumps(xml_dict))
print(type(xml_dict2))
print(xml_dict2)
print("*" * 80)
for country in xml_dict2["data"]["country"]:
    print("name : {}".format(country["@name"]))
    print("rank : {}".format(country["rank"]))
    print("year : {}".format(country["year"]))
    print("gdppc : {}".format(country["gdppc"]))
    print("neighbor : {}".format(country["neighbor"]))
    if type(country["neighbor"])==list:
        for neighbor in country["neighbor"]:
            print("neighbor : {}, {}".format(neighbor["@name"], neighbor["@direction"]))
    else:
        print("neighbor : {}, {}".format(country["neighbor"]["@name"], country["neighbor"]["@direction"]))
    print("-" * 80)
print("*" * 80)
