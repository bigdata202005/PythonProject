# 시퀀스객체[시작인덱스:끝인덱스:인덱스증가폭]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[2:8:2])
print(list1[2:8:4])
print(list1[3::3])
print(list1[::2])  # 처음부터 끝까지 2칸씩 [0, 2, 4, 6, 8]
print(list1[::-2])  # 뒤에서 부터 2칸씩 [9, 7, 5, 3, 1]
print(list1[::-1])
a = 1234
print(str(a)[::])  # 전체 : 1234
print(str(a)[::-1])  # 전체 : 4321
print(str(a)[::-2])  # 42

str1 = "Hello World!!"
print(str1[::-1])
print(len(str1))
print(str1[10:11])
print(str1[15:16])
print(str1[16:17])
