"""
CSV 파일과 비슷하지만, 콤마 대신 Tab으로 컬럼을 분리하는 파일포맷을 TSV 파일이라 한다.
TSV 파일은 컬럼 delimiter만 차이가 나므로, csv 모듈의 reader() 혹은 writer() 함수에서 delimiter='\t'
옵션만 지정해 주면 나머지는 CSV와 동일하다.
"""
import csv

# .tsv 읽기
file = open('data.tsv', 'r', encoding='utf-8', newline='')
reader = csv.reader(file, delimiter='\t')
print(reader)
str_list = list(reader)
print(str_list)
for data in str_list:
    print("{}. {}({})".format(data[0], data[1], data[2] == 'True' and "남자" or "여자"))
file.close()
