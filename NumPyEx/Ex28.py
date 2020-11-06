import numpy as np

# ix_ () 함수
# 이 ix_함수는 각 n-uplet에 대한 결과를 얻기 위해 다른 벡터를 결합하는 데 사용할 수 있습니다.
# 예를 들어, 각 벡터 a, b 및 c에서 가져온 모든 트리플렛에 대해 모든 a + b * c를 계산하려는 경우 :

a = np.array([2, 3, 4, 5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8, 3])
ax, bx, cx = np.ix_(a, b, c)
print(ax)
print("~" * 80)

print(bx)
print("~" * 80)

print(cx)
print("~" * 80)

print(ax.shape, bx.shape, cx.shape)
print("~" * 80)

result = ax + bx * cx
print(result)
print(result.shape)
print("~" * 80)
