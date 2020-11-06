import numpy as np


def line(count=30):
    print("~" * count)


def view_array(array):
    print(type(array))
    print(array.dtype)
    print(array)
    line()


# 숫자 시퀀스를 만들기 위해 NumPy는 arange
# Python 내장 함수와 유사한 함수를 제공 range하지만 배열을 반환합니다.
array1 = np.arange(10, 30, 5)  # arange(시작, 종료, 증감)
view_array(array1)

array2 = np.arange(2, 3, 0.3)  # arange(시작, 종료, 증감)
view_array(array2)

array3 = np.arange(3, 2, -0.3)  # arange(시작, 종료, 증감)
view_array(array3)

# linspace : 단계 대신 원하는 요소 수를 인수로받는 함수
array4 = np.linspace(2, 3, 5)  # linspace(시작, 종료, 개수)
view_array(array4)

array5 = np.linspace(2, 3, 3)
view_array(array5)
