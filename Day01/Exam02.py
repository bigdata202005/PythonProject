# 문제 : 생년월일을 8자리 정수로 입력받아 년월일을 구분하여 출력하시오!!!!
birth = int(input("생년월일을 8자리 정수로 입력 : "))
year = birth // 10000
month = birth // 100 % 100
day = birth % 100
print("{0:04d}년 {1:02d}월 {2:02d}일".format(year, month, day))


