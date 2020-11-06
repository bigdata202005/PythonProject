import numpy as np
from numpy import newaxis

# 다른 배열을 함께 쌓기
rg = np.random.default_rng()  # 난수 발생기 객체 생성
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))
print("2차원 배열의 경우")
print('=' * 80)
print("a배열")
print(a)
print('~' * 80)

print("b배열")
print(b)
print('~' * 80)

ar1 = np.column_stack((a, b))  # 열로 붙이기
print(ar1)
print('~' * 80)

print("1차원 배열의 경우")
print('=' * 80)

# 1차원  배열
a = np.array([4., 2.])
b = np.array([3., 8.])
print("a배열")
print(a)
print('~' * 80)

print("b배열")
print(b)
print('~' * 80)
ar1 = np.column_stack((a, b))
print(ar1)
print('~' * 80)
"""
열이 행으로 변하고 옆으로 붙었다
[[4. 3.]
 [2. 8.]]
"""
ar1 = np.hstack((a, b))  # 옆으로 붙이려면 hstack을 사용해라!!
print(ar1)
print('~' * 80)

ar2 = a[:, newaxis]  # 열을 행으로 바꿈
print(ar2)
print('~' * 80)

# ar3 = np.column_stack((a[:, newaxis], b[:, newaxis]))
ar3 = np.column_stack((a, b))
print(ar3)
print('~' * 80)

# hstack으로 column_stack처럼 사용하려면 축을 변경하면 된다.
ar4 = np.hstack((a[:, newaxis], b[:, newaxis]))
print(ar4)
print('=' * 80)

# 반면에이 함수 row_stack는 vstack 모든 입력 배열 과 동일 합니다.
# 사실 row_stack은의 별칭입니다 vstack.
print("1차원 배열의 경우 : vstack, row_stack")
ar5 = np.vstack((a, b))
print(ar5)
print('~' * 80)

ar6 = np.row_stack((a, b))
print(ar6)
print('~' * 80)


print("2차원 배열의 경우 : vstack, row_stack")
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))
ar5 = np.vstack((a, b))
print(ar5)
print('~' * 80)

ar6 = np.row_stack((a, b))
print(ar6)
print('~' * 80)