import numpy as np

# ...
c = np.array([[[0, 1, 2],  # a 3D array (two stacked 2D arrays)
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(str(c.ndim) + '차원 배열')  # 3
print(c.shape)  # 2 * 2 * 3
print(c.size)  # 12
print(c)
print("~" * 80)
print(c[0])
print("~" * 80)
print(c[1])
print("~" * 80)
print(c[0, 1])
print("~" * 80)

print(c[1, ...])
"""
[[100 101 102]
 [110 112 113]]
"""
print("~" * 80)

# 2차원 배열의 세번째 열값들만
print(c[..., 2])
"""
[[  2  13]
 [102 113]]
"""
print("~" * 80)
print(c[..., -2])
print("~" * 80)
print(c[..., 1])
print("~" * 80)


# 반복
for i in c:
    for j in i:
        for k in j:
            print(k, end='-')
        print()
    print('-' * 20)
print('=' * 20)


