# 리스트명 = [요소1, 요소2, 요소3, ...]
odd = [1, 3, 5, 7, 9]
print(odd)
print(odd[0])
print(odd[1])
print(odd[2])
print(odd[3])
print(odd[4])
# print(odd[5])  # IndexError: list index out of range
a = []  # 빈 리스트 만들기
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(a, b, c, d, e)
print(e[2][1])
f = list()
print(f)  # 빈 리스트 만들기
