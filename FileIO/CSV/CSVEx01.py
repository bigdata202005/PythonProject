"""
CSV란 Comma-separated values의 약자로서 CSV 파일은 각 라인의 컬럼들이 콤마로 분리된 텍스트 파일 포맷이다.
가장 간단한 형태의 CSV 파일은 문자열을 콤마로 Split 하여 처리하면 되지만,
간혹 컬럼 데이타에 콤마가 있을 경우 이중인용부호로 감싸서 데이타 내의 콤마를 Escape하기 (예: "Lee, Alex")
때문에, 파이썬에 내장된 csv 모듈을 사용하여 .csv 파일을 처리하는 것이 좋다.""
"""
import csv

file = open('data.csv', 'r', encoding='utf-8')  # 파일 오픈
reader = csv.reader(file) # reader함수로 읽기
print(type(reader), reader)
for line in reader:
    print(line, line[1], line[3])
file.close()
