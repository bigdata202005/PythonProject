# json 파일 읽기
import json
# 인코딩이 다르면 읽기 실패!!!
# with open('dic.json', 'r', encoding="utf-8") as json_file:
with open('dic.json', 'r', encoding="utf-8-sig") as json_file:
    json_data = json.load(json_file)
    print(type(json_data))
    print(len(json_data), "개", sep="")

    for hanja in json_data:
        print(hanja)
    print("-" * 80)

    for hanja in json_data:
        print("{:04d}. {}({} {})".format(hanja["n"], hanja["h"], hanja["m"], hanja["m1"]))


