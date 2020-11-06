import numpy as np

# 인덱싱, 슬라이싱 및 반복
a = np.arange(10) ** 3
print(a)
print(a[2])     # 세번째 요소
print(a[2:5])   # 2~4까지
print(a[:])     # 전체
print(a[4:])    # 다삿번쨰 부터 끝까지
print(a[:4])    # 0번 부터 4전까지

a[:6:2] = 1000 # 0~5까지 2칸씩 띄어서 값수정
print("~"*80)

print(a)
print("~"*80)

print(a[::-1])  # 배열 뒤집기
print("~"*80)
b = a[::-1]  # 원본이 변경되지 않는다.
# 반복
for i in a:
    print(i, end=' ')
print()
for i in b:
    print(i, end=' ')
print()
