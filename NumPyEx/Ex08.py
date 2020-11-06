import numpy as np


def line(count=30):
    print("~" * count)


# 배열의 합, 최대값, 최소값
a = np.random.randint(1, 21, 12).reshape(3, 4)
print(a)
line()
print(a.sum(), a.max(), a.min())
line()

# 축값지정
print(a.sum(axis=0))  # 세로합
print(a.sum(axis=1))  # 가로합
line()

print(a.min(axis=0))
print(a.min(axis=1))
line()

print(a.max(axis=0))
print(a.max(axis=1))
line()

print(a)
print("각 행의 누적 합계")
print(a.cumsum(axis=1))
line()

print(a)
print("각 열의 누적 합계")
print(a.cumsum(axis=0))
line()
