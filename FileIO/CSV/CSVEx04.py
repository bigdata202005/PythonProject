import csv

with open('person.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['name', 'age', 'gender']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': '한사람', 'age': 33, 'gender': True})
    writer.writerow({'name': '두사람', 'age': 23, 'gender': False})
    writer.writerow({'name': '세사람', 'age': 18, 'gender': True})
    writer.writerow({'name': '네사람', 'age': 45, 'gender': False})
print("저장완료!!!")

with open('./person.csv', 'r', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for data in reader:
        print("{}씨({}세, {})".format(data['name'], data['age'], data['gender']=='True' and "남자" or "여자", ))