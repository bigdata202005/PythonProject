# lambda
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
# 보통 함수를 한줄로 간결하게 만들 때 사용한다.
# 우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.
#
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b: a + b
print(add(10, 20))

myMax = lambda a, b: a > b and a or b
myMin = lambda a, b: a < b and a or b

list1 = [8, 1, 7, 2, 9, 5, 4, 6, 3]
maxVal = minVal = list1[0]
for n in list1:
    maxVal = myMax(maxVal, n)
    minVal = myMin(minVal, n)

print("최대값 : ", maxVal)
print("최소값 : ", minVal)

