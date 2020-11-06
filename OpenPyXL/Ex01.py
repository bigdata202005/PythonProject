# Excel 파일 다루기
# pip install openpyxl  ==> 설치
from openpyxl import Workbook
# 엑셀문서 만들기
wb = Workbook()

# 저장하기
wb.save("Ex01.xlsx")
