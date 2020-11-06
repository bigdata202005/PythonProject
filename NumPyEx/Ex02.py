import numpy as np


def line(count=30):
    print("~" * count)


def view_array(array):
    print(type(array))
    print(array.dtype)
    print(array)
    line()


# 배열 생성 : 배열을 만드는 방법에는 여러 가지가 있습니다.
array1 = np.array([2, 3, 4])
print(type(array1))
print(array1.dtype)
print(array1)
print(array1[0], array1[1], array1[2])
for n in array1:
    print(n, end=' ')
print()
line()

# 주의 : TypeError발생!!!
# array2 = np.array(2, 3, 4)

array2 = np.array((2, 3, 4))
view_array(array2)

array3 = np.array([1.2, 3.5, 5.1])
view_array(array3)

# float64로 자동으로 변경
array4 = np.array([(1.5, 2, 3), (4, 5, 6)])
view_array(array4)

# int32타입을 생성
array5 = np.array([[1, 2], [3, 4]])
view_array(array5)

# int64타입을 생성
array6 = np.array([[1, 2], [3, 4]], dtype=np.int64)
view_array(array6)

# complex(복소수) 타입을 생성
array7 = np.array([[1, 2], [3, 4]], dtype=complex)
view_array(array7)

# 0으로 초기화
array8 = np.zeros((3, 4))
view_array(array8)

# 2 * 3 * 4의 3차원 배열을 만들고 1로 초기화
array9 = np.ones((2, 3, 4), dtype=np.int16)
view_array(array9)

# 빈 배열 생성. 쓰레기값 할당
array10 = np.empty((2, 4))
view_array(array10)

# 숫자 시퀀스를 만들기 위해 NumPy는 arangePython 내장 함수와 유사한 함수를 제공 range하지만 배열을 반환합니다.
# arange(시작값, 종료값, 간격)
array11 = np.arange(10, 30, 5).reshape(2, 2)
print(array11)
