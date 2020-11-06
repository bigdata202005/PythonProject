import Day04.mod1

print(Day04.mod1.add(4, 5))
print(Day04.mod1.sub(11, 5))


# from 모듈이름 import 모듈함수
from Day04.mod1 import add
from Day04.mod1 import sub

print(add(4, 5))
print(sub(4, 5))


from Day04.mod1 import add, sub
print(add(4, 5))
print(sub(4, 5))


from Day04.mod1 import *
print(add(4, 5))
print(sub(4, 5))
