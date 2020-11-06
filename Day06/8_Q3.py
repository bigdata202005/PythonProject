"""
Q3 리스트의 더하기와 extend 함수
다음과 같은 리스트 a가 있다.

a = [1, 2, 3]
리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.

a = [1, 2, 3]
a = a + [4,5]
a
[1, 2, 3, 4, 5]
리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.

a = [1, 2, 3]
a.extend([4, 5])
a
[1, 2, 3, 4, 5]
+ 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.
"""
a = [1, 2, 3]
print(a)
a += [4, 5]
print(a)

b = [1, 2, 3]
print(b)
b.extend([4, 5])
print(b)

c = [1, 2, 3]
def fn1():
   # c = c + [4, 5]  # 이부분 에러 c리스트 사용 못함
   print("+ 사용 못함")

def fn2():
    c.extend([4, 5]) # extend는 사용가능

print(c)
fn1()
print(c)
fn2()
print(c)
