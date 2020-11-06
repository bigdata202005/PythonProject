import csv
import json

in_file = open('chunja2.csv', 'r', encoding='utf-8', newline='')
out_file = open('chunja2.json', 'w', encoding='utf-8')

reader = csv.DictReader(in_file)
hanja_list = list()
for hanja in reader:
    hanja_list.append({"idx":hanja["idx"], "h":hanja["h"], "k":hanja["k"], "m":hanja["m"], "m1":hanja["m1"]})
print(len(hanja_list))

# ensure_ascii = False를 생략시 한글이 유니코드로 저장됨!!!
json.dump(hanja_list, out_file,  ensure_ascii = False)
in_file.close()
out_file.close()

with open('천자문2.json', 'w', encoding='UTF-8-sig') as file:
   file.write(json.dumps(hanja_list, ensure_ascii=False))

