import numpy as np


def line(count=30):
    print("~" * count)


# 배열의 타입 변환
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)
print(a.dtype.name)
print(a)
print(b.dtype.name)
print(b)
c = a + b  # 큰 타입으로 자동 형변환
print(c.dtype.name)
print(c)

# NumPy의 np.exp() 함수는 밑(base)이 자연상수 e인 지수함수 y = e ** x 로 변환해줍니다.
d = np.exp(c * 1j)
print(d.dtype.name)
print(d)
line()

# 복소수
complex1 = 1 + 2j
complex2 = 3j
complex3 = complex1 + complex2
complex4 = complex1 * complex2
"""
(1+2j) * (3j)
= (1*3j) + 2j*3j
= 3j + 6j**2
= -6 + 3j
"""
print(type(complex1), complex1)
print(type(complex2), complex2)
print(type(complex3), complex3)
print(type(complex4), complex4)


