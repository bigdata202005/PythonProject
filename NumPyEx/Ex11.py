import numpy as np


def fn(row, col):
    return 10 * row + col


# 함수를 이용하여 배열 생성
# fromfunction(함수, 행렬크기, 타입)
ar = np.fromfunction(fn, (5, 4), dtype=int)
print(ar)

# 함수 대신에 람다식도 가능하다.
ar2 = np.fromfunction(lambda row, col: 10 * row + col, (5, 4), dtype=int)
print(ar2)
print("~" * 80)

# 다차원 배열 인덱싱
print(ar[2, 3])  # 대괄호 대신 ,(콤마)를 사용한다. 3행 4열의 값
print("~" * 80)
# 1개의 열 전체
print(ar[0:5, 1])  # 2번째 열 0~4행의 값
print(ar[:, 2])  # 3번째 열 0~4행의 값
print("~" * 80)
# 1개의 행 전체
print(ar[0, :])
print(ar[1, :])
print(ar[2, :])
print("~" * 80)

# 차원수보다 적은 첨자는 전체를 의미한다.
# 2차원 배열에서 첨자를 1개만 지정하면 행전체가 된다.
print(ar[-1])   # 마지막행
print(ar[0])    # 첫번째 행



