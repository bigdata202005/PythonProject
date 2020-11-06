import csv
# with절 사용하기
with open('./data2.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # 1줄제거
    # print(header)
    for data in reader:
        print("{}. {}씨".format(data[0], data[1]))  # reader로 읽기하면 첨자로 접근

print("-" * 80)
# 데이터의 첫줄이 key인경우 DictReader로 읽는다.
with open('./data2.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for data in reader: # DictReader로 읽으면 첫줄을 키로 사용해서 dict가 된다.
        print("{}. {}씨".format(data['id'], data['name']))
print("-" * 80)

