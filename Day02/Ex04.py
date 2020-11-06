# 튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.
#
# 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(type(t5))

# t2[0] = 3  # TypeError: 'tuple' object does not support item assignment 변경 금지
# del t5[2]   # TypeError: 'tuple' object doesn't support item deletion 삭제 금지
print(t2)

# 인덱싱
print(t5[1])
print(t5[-2])
print(t5[-1][1])

# 슬라이싱
print(t5[:])
print(t5[:2])
print(t5[1:])
print(t5[1:2])

# 더하기
t1 = (1, 2, 3)
t2 = ('a', 'b')
t3 = t1 + t2
print(t1, t2, t3)
# 곱하기
t4 = t2 * 5
print(t4)
# 길이 구하기
print(len(t4))

