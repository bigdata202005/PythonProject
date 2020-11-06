# https://openpyxl.readthedocs.io/en/stable/tutorial.html 참조!!!
from openpyxl import Workbook
# Workbook 오브젝트 생성
wb = Workbook()
print(wb)
# 저장하기 : 빈문서
wb.save("ex01.xlsx")
