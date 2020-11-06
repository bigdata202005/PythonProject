# Excel 파일 다루기
from openpyxl import load_workbook

# 엑셀 문서 읽기
wb = load_workbook('ex09.xlsx')
print(wb)
ws = wb.active

print("ex09.xlsx파일 내용")
print("~" * 80)
# 값만 모두 읽기 : ws.values
for row in ws.values:
    for value in row:
        print(value, end=' ')
    print()
print("~" * 80)
# 읽어서 리스트로 만들기
lotto_list = []
for row in ws.values:
    lotto = []
    for value in row:
        lotto.append(value)
    lotto.sort() # 정렬
    lotto.append(sum(lotto))  # 가로 합계 추가
    lotto_list.append(lotto)

print(lotto_list)

# 다른이름으로 저장
wb.save('Ex10.xlsx')
