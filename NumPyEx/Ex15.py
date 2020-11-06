import numpy as np

# 다른 배열을 함께 쌓기
rg = np.random.default_rng()  # 난수 발생기 객체 생성
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))
print("a배열")
print(a)
print('~' * 80)

print("b배열")
print(b)
print('~' * 80)

ar1 = np.vstack((a, b))  # 행으로 붙이기
print("ar1배열 : vstack")
print(ar1)
print('~' * 80)

ar2 = np.hstack((a, b)) # 열로 붙이기
print("ar2배열 : hstack")
print(ar2)
print('~' * 80)
print("원본은 변하지 않는다.")
print("a배열")
print(a)
print('~' * 80)

print("b배열")
print(b)
print('~' * 80)





