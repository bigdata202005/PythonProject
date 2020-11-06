import numpy as np

# 배열 생성
ar = np.fromfunction(lambda row, col: row * 3 + col + 1, (3, 3), dtype=int)
print(ar)
print("~" * 80)
# 행반복
for row in ar:
    print(row)
print("~" * 80)
# 행열반복
for row in ar:
    for col in row:
        print(col)
print("~" * 80)
# 데이터 전체를 반복할때는 flat 속성을 사용한다.
for data in ar.flat:
    print(data)
print("~" * 80)

# 3차원 배열도 가능하다.
ar2 = np.arange(1, 19).reshape(2, 3, 3)
print(ar2.ndim, "차원 배열", sep='')
print(ar2.shape)
for data in ar2.flat:
    print(data)
print("~" * 80)
