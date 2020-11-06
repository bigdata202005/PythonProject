# 라이브러리
# sys
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
import sys
print(sys.argv)

"""
Day05> python Ex02.py 1 2 3 4 5
['Ex02.py', '1', '2', '3', '4', '5']
"""
print(sys.path)
print()
for p in sys.path:
    print(p)

print("-" * 80)
for fn in dir(sys):
    print(fn)
print("-" * 80)


