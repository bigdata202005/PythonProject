# 고급 인덱싱 및 인덱스 트릭
# 부울배열을 인수로
import numpy as np

a = np.arange(12).reshape(3, 4)
b = a > 4  # 조건의 결과를 부울식 배열로 만들어 준다.
print("배열 a")
print(a)
print("배열 b")
print(b)
print("배열 : a[b]")
print(a[b])  # b배열의 True인 위치의 값만 가져온다.
print("~" * 80)
print(a[a % 2 == 0])  # 짝수만
print("~" * 80)
print(a[a % 2 != 0])  # 홀수만


# 부울배열로 값을 변경도 가능하다
a[b] = 0

print("배열 a")
print(a)