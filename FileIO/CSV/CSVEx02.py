import csv
# 파일을 쓰기용으로 오픈
file = open('output.csv', 'w', encoding='utf-8', newline='')
# writer 객체 얻기
writer = csv.writer(file)
# writerow함수로 1줄 저장
writer.writerow([1, "김정수", False])
writer.writerow([2, "박상미", True])
writer.writerow((3, "한사람", False))
writer.writerow((4, "두사람", False))
# 닫기
file.close()
print("저장완료!!!")
