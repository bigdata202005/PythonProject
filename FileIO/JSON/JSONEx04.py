# json 파일 출력하기
import json

car_group = dict()
k5 = dict()
k5["price"] = "5000"
k5["year"] = "2015"
car_group["K5"] = k5

avante = dict()
avante["price"] = "3000"
avante["year"] = "2014"
car_group["Avante"] = avante

morning = dict()
morning["price"] = "1500"
morning["year"] = "2020"
car_group["Morning"] = morning

# json 파일로 저장
with open('test.json', 'w', encoding='utf-8') as make_file:
    json.dump(car_group, make_file, indent="\t")

# 저장한 파일 출력하기
with open('test.json', 'r') as f:
    json_data = json.load(f)

print(json.dumps(json_data, indent="\t"))