import numpy as np
from numpy import newaxis

# 복잡한 경우에, r_그리고 c_하나 개의 축을 따라 번호를 적층하여
# 배열을 만들 때 유용하다. 범위 리터럴 ( ":")을 사용할 수 있습니다.
ar1 = np.r_[1:4, 0, 4]
print(ar1)
print('~' * 80)

ar1 = np.r_[np.array([1, 2, 3]), 0, 0, np.array([4, 5, 6])]
print(ar1)
print('~' * 80)

ar1 = np.r_[-1:1:6j, [0] * 3, 5, 6]
print(ar1)
print('~' * 80)

# 문자열 정수는 연결할 축 또는 항목을 강제 적용 할 최소 차원 수를 지정합니다.
ar1 = np.array([[0, 1, 2], [3, 4, 5]])
ar1 = np.r_['-1', ar1, ar1]
print(ar1)
print('~' * 80)

print("'0,2'사용")
ar1 = np.r_['0,2', [1, 2, 3], [4, 5, 6]]
print(ar1)
print('~' * 80)

print("'0,2,0'사용")
ar1 = np.r_['0,2,0', [1, 2, 3], [4, 5, 6]]
print(ar1)
print('~' * 80)

print("'1,2,0'사용")
ar1 = np.r_['1,2,0', [1, 2, 3], [4, 5, 6]]
print(ar1)
print('~' * 80)

# 'r'또는 'c'를 첫 번째 문자열 인수로 사용하면 행렬이 생성됩니다.
ar1 = np.r_['r', [1, 2, 3], [4, 5, 6]]
print("'r'사용")
print(ar1)
print('~' * 80)

print("'c'사용")
ar1 = np.r_['c', [1, 2, 3], [4, 5, 6]]
print(ar1)
print('~' * 80)