a = [1, 2, 3]
b = a  # 참조형이네!!!! ===> 얕은 복사 : 주소가 복사
c = [1, 2, 3]
print(a)
print(b)
print(c)
a.append(99)  # a에 추가
print(a)
print(b)  # 둘다 변경됨
print(c)
# id함수 : 자바의 해시코드와 같이 객체를 구분하는 번호를 알려준다.
print(id(a))
print(id(b))
print(id(c))

# is 연산자 : 객은 객체를 가리키는지 판단해주는 연산자.
print(a is b)
print(a is c)
print(c is a)

# 깊은 복사 : 내용이 복사
d = a[:]
print()
print(a)
print(d)
d.append(77)
d.append(66)
print(a)
print(d)  # d만 변경
# 부분 복사
e = d[3:]
print(e)
e.append(11)
e.append(22)
print(e)

