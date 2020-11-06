"""
CSV 파일과 비슷하지만, 콤마 대신 Tab으로 컬럼을 분리하는 파일포맷을 TSV 파일이라 한다.
TSV 파일은 컬럼 delimiter만 차이가 나므로, csv 모듈의 reader() 혹은 writer() 함수에서 delimiter='\t'
옵션만 지정해 주면 나머지는 CSV와 동일하다.
"""
import csv

# .tsv 쓰기
file = open('data.tsv', 'w', encoding='utf-8', newline='')

writer = csv.writer(file, delimiter='\t')
writer.writerow([1, "김정수", False])
writer.writerow([2, "박상미", True])
writer.writerow((3, "한사람", False))
writer.writerow((4, "두사람", False))
file.close()
