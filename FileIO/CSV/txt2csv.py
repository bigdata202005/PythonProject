import csv

file = open('chunja.txt', 'r', encoding='utf-8')

out_file = open('chunja.csv', 'w', encoding='utf-8', newline='')
fieldnames = ['idx', 'h', 'm', 'm1']
writer = csv.DictWriter(out_file, fieldnames=fieldnames)
writer.writeheader()

reader = csv.reader(file, delimiter='|')
for hanja in reader:
    print(hanja)
    writer.writerow({'idx': hanja[0], 'h': hanja[1], 'm': hanja[2], "m1": hanja[3]})

file.close()
out_file.close()

# 데이터의 첫줄이 key인경우 DictReader로 읽는다.
with open('chunja.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for data in reader: # DictReader로 읽으면 첫줄을 키로 사용해서 dict가 된다.
        print("{}. {}".format(data['idx'], data['h']))
print("-" * 80)

