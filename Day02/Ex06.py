# 집합 자료형은 어떻게 만들까?
# 집합(set)은 파이썬 2.3부터 지원하기 시작한 자료형으로,
# 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).

# 집합 자료형은 다음과 같이 set 키워드를 사용해 만들 수 있다.
#
s1 = set([1, 2, 3])
print(s1)
print(type(s1))

s2 = set("Hello World!!!!")
print(s2)
print(type(s2))

# print(s2[0])   # TypeError: 'set' object is not subscriptable
t2 = tuple(s2)
print(t2)
print(t2[0])
print(len(t2))

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
s2 = set([1, 3, 5, 7, 9])
s3 = set([2, 4, 6, 8])
print(s1)
print(s2)
print(s3)
# 합집합
s4 = s2 | s3
print(s4)
# 교집합
s5 = s1 & s3
print(s5)
# 차집합
s6 = s1 - s3
print(s6)

# 값 1개 추가하기(add)
s6.add(99)
s6.add(88)
s6.add(77)
print(s6)

# 값 여러개 추가하기(update)
s6.update([1, 2, 3, 4, 66])
print(s6)

# 특정 값 제거하기(remove)
s6.remove(88)
s6.remove(66)
# s6.remove(55)  # s6.remove(55) KeyError: 55
print(s6)
