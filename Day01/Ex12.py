# 문자열 자르기
birth = "1234567890"
print(birth[3])  # 숫자 1개면 인덱스 값(zero base) : 4
print(birth[3:])  # 이후 모든 문자 : 4567890
print(birth[:3])  # 이전 문자 : 123
print(birth[2:5])  # 시작:종료  : 345
print(birth[:])  # 모두
print(birth)  # 모두

birth = "19990205"
year = birth[:4]
month = birth[4:6]
day = birth[6:]
print("{0}년 {1}월 {2}일".format(year, month, day))
print(birth[-1])
print(birth[-2])
print(birth[-3])
print(birth[4:-2])  # 02 : birth[4] ~ birth[-2]
print(birth[3:-2])  # 902
print(birth[6:])  # 902

