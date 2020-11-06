# 외장모듈인 xmltodict를 이용하는 방법
# !pip install xmltodict # 미설치된 경우 설치한다
import xmltodict
import json

str_xml = '''<animals>
                <animal>
                    <name>lion</name>
                    <lifespan>13</lifespan>
                </animal>
                <animal>
                    <name>tiger</name>
                    <lifespan>17</lifespan>
                </animal>
            </animals>'''
cc = xmltodict.parse(str_xml)  # return collections.OrderedDict
print(type(cc))
print(cc)
print("*" * 80)
print(type(json.dumps(cc)))
print(json.dumps(cc))
print("*" * 80)
dd = json.loads(json.dumps(cc))  # return dict
print(type(dd))
print(dd)
print("*" * 80)

animals = dd['animals']['animal']
print(animals)  # 결과를 출력한다
for ani in animals:
    print(ani["name"],"(", ani["lifespan"], ")", sep="")