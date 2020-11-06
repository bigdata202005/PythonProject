# "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
str1 = "Pithon"
print(str1)

# 문자열은 불변객체이다.
# str[1] = 'y'
# print(str)  # TypeError: 'str' object does not support item assignment

print(str1[0] + 'y' + str1[2:])

age = 30
str2 = "당신의 나이는 {}살입니다.".format(age)
print(str2)
str3 = "당신의 내년 나이는 {}살입니다.".format(age+1)
print(str3)
str4 = f"당신의 내년 나이는 {age+1}살입니다."
print(str4)

# print(str(range(1,10001)).count('8'))
print(range(1, 10001))  # 범위 자료형
print(list(range(1, 10001)))  # 리스트로 변환
print(str(list(range(1, 10001))))  # 문자열로 변환
# 문자열 중에 8의 개수 세기
print(str(list(range(1, 10001))).count("8"), "개", sep="")

age = 33
#  print(age + '세')  # Error : int와 str을 더할 수 없다.
print(str(age) + '세')
print(age, '세', sep="")

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

