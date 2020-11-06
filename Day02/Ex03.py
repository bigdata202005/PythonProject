# 리스트의 연산
# 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a)
print(b)
print(c)  # [1, 2, 3, 4, 5, 6]

# 리스트 곱하기
d = a * 4
print(d)  # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#  리스트 길이 구하기
print(len(a))  # 3
print(len(c))  # 6
print(len(d))  # 12

# [초보자가 범하기 쉬운 리스트 연산 오류]
# print(a[2] + "Hi")  # 에러!!! 숫자와 문자 연산했기 때문
print(str(a[2]) + "Hi")

# 리스트의 수정과 삭제
print(a)
a[1] = 99  # 수정
print(a)
del a[1]  # 삭제
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(a)
del a[5:]  # 범위 삭제
print(a)

# 리스트에 요소 추가(append)
c = list()
print(c)
c.append(1)
c.append(2)
print(c)
del c[:]  # 모두 삭제
print(c)
# 반복문으로 추가
for i in range(1, 11):
    c.append(i)
print(c)

# 리스트 정렬(sort)
d = [3, 2, 5, 1, 6, 4]
print(d)
d.sort()
print(d)
# 리스트 뒤집기(reverse)
d.reverse()
print(d)

# 위치 반환(index)
# index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
# print(d.index(0))  # ValueError: 0 is not in list 값이 없어서 에러
print(d.index(5))

# 리스트에 요소 삽입(insert)
print(d)
d.insert(3, 88)
d.insert(3, 99)
print(d)

# 리스트 요소 제거(remove)
# remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.
d.remove(6)
print(d)
d.remove(3)
print(d)

# 리스트 요소 끄집어내기(pop)
print(d.pop())  # 뒤에서 1개 꺼내서 제거
print(d.pop())
print(d)
print(d.pop(1))  # 지정 위치에서 1개 꺼내서 제거
print(d)

# 리스트에 포함된 요소 x의 개수 세기(count)
d = [1, 2, 1, 2, 1, 2, 1, 2, 1, 3, 4]
print("2의 개수 : " + str(d.count(2)) + "개")

# 리스트 확장(extend)
# extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.
list1 = [1, 2, 3]
list2 = [11, 22, 33, 44]
print(list1)
print(list2)

list1.extend(list2)
print(list1)
print(list2)

list3 = list1 + list2
print(list3)

