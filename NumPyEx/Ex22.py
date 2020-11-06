# 고급 인덱싱 및 인덱스 트릭
# 배열은 정수 배열과 부울 배열로 인덱싱 할 수 있습니다.
import numpy as np

# 둘 이상의 차원에 대한 인덱스를 제공 할 수도 있습니다.
# 각 차원에 대한 인덱스 배열의 모양은 동일해야합니다.
a = np.arange(12).reshape(3, 4)
print(a)
print("~" * 80)
                   
i = np.array([[0, 1], [1, 2]])  # x 좌표값
j = np.array([[2, 1], [3, 3]])  # y 좌표값


print(a[i])
print("~" * 80)
print(a[i, j])
print("~" * 80)
print(a[i, 2])  # y 좌표를 2로 고정
print("~" * 80)
print(a[:, j])  # a배열 전체와 j배열을 인덱싱 : 3차원이 나온다.
print("~" * 80)

# 인수를 튜플로 전달해도 된다.
l = (i, j)
print(a[l])
print("~" * 80)


s = np.array([i, j])
# 아래는 에러 발생 : 인수로 numpy배열을 넘기면 에러
# IndexError: index 3 is out of bounds for axis 0 with size 3
# print(a[s])
print(s)    # 3차원 배열
print("~" * 80)
print(tuple(s))  # 2차원 배열
print("~" * 80)

print(a[tuple(s)]) # 튜플로 만들어 넘기면 정상 작동
print("~" * 80)
