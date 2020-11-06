import numpy as np


def line(count=30):
    print("~" * count)


# 범용함수
a = np.arange(1, 5)
print(a)
line()
# 지수함수
b = np.exp(a)
print(b)
line()
# 제곱근
c = np.sqrt(a)
print(c)
line()

d = np.array([11, 22, 33, 44])
e = np.add(a, d)
print(a)
print(d)
print(e)
line()




f = list(map(lambda x: "{:02d} ".format(x), a))
print(type(f))
print(f)
