from copy import copy

a = [1, 2, 3, 4]
b = copy(a)  # copy 모듈을 이용한 깊은 복사
print(a)
print(b)
print(a is b)
b.append(44)
b.extend([66, 77, 88])
print(a)
print(b)
print('*' * 60)

i, j = (11, 22)
print(i, j)
(i, j) = 44, 55
print(i, j)

i, j = j, i  # 교환
print(i, j)

k = l = m = 999  # 값 할당
print(k, l, m)
