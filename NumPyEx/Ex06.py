import numpy as np


def line(count=30):
    print("~" * count)


# +=, *= 새로운 하나를 만드는 것보다 기존 배열을 수정합니다.
rg = np.random.default_rng(1)  # 난수 발생기 객체 선언
print(rg.random(5))  # 난수 5개
print(np.random.randint(1, 45, size=6))  # 난수 6개
line()

a = np.ones((2, 3), dtype=int)  # 2행 3열을 1로 초기화 해서 2차원 배열 생성
b = rg.random((2, 3))  # 2행 3열을 난수로 초기화 해서 2차원 배열 생성
print(a)
print(b)
line()

a += 3
print(a)  # 기존 배열을 수정
line()

b *= 100
print(b)
line()

