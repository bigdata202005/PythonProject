# Excel 파일 다루기
from openpyxl import Workbook
import datetime
# 엑셀문서 만들기
wb = Workbook()
# 워크시트 선택
ws = wb.active
# 값 추가
for row in range(1, 11):
    ws.append(range(10))
# 값만 모두 읽기 : ws.values
for row in ws.values:
    for value in row:
        print(value, end=' ')
    print()
print("~" * 80)
# 저장하기
wb.save("Ex08.xlsx")
