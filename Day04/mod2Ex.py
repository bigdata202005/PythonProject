from Day04.mod2 import *

print("원주율 :", PI)
math = Math()
print("반지름 7인 원의 넓이 :", math.solv(r=7))
print("{} + {} = {}".format(5, 8, add(5, 8)))

# 무수히 많은 내잔 모듈들이 존재한다.
import sys

print(sys.path)
print("-" * 80)
for path in sys.path:
    print(path)
