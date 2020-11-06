# 사용자 입력과 출력
#  name = input()
name = input("이름 : ")
print("당신의 이름은 '" + name + "'입니다.")
age = input("나이 : ")
print("{}씨의 나이는 {}세입니다.".format(name, age))
print(type(age))
# print("{}씨의 내년 나이는 {}세입니다.".format(name, age+1)) # 기본 입력은 str이다. 타입에러!!!
age = int(input("나이 : "))
print("{}씨의 내년 나이는 {}세입니다.".format(name, age+1))
print(type(age))
