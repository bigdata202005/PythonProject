# json 파일 읽기
import json

with open('test.json', 'r') as json_file:
    json_data = json.load(json_file)

print(type(json_data))
print(json_data)
print("-" * 80)
print("K5 : 가격({}만원), {}년식 ".format(json_data['K5']['price'], json_data['K5']['year']))
for car_dict in json_data:
    print("{} : 가격({}만원), {}년식 ".format(car_dict,json_data[car_dict]['price'], json_data[car_dict]['year']))
print("-" * 80)

with open('test.json', 'r') as json_file:
    json_data = json.load(json_file)
print(json.dumps(json_data, indent="\t", sort_keys=True))