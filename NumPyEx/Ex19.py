import numpy as np

# 하나의 배열을 여러 개의 작은 배열로 나누기
rg = np.random.default_rng()
ar1 = np.floor(10*rg.random((12, 2)))  # 12행 2열 배열을 난수로 만듬
print(ar1)
print("-" * 80)

print("np.vsplit(ar1, 3)")
ar2 = np.vsplit(ar1, 3)
print(ar2)
print("-" * 80)
for ar in ar2:
    print(ar)
print("-" * 80)

print("np.vsplit(ar1, (3, 7)")
ar2 = np.vsplit(ar1, (3, 7))
print(ar2)
print("-" * 80)
for ar in ar2:
    print(ar)
print("-" * 80)

