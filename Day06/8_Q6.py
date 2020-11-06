"""
Q6 숫자의 총합 구하기
사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오.
(단 숫자는 콤마로 구분하여 입력한다.)

65,45,2,3,45,8
"""
data = input("숫자를 콤마로 구분하여 입력 : ")
str_list = data.split(",")
print(str_list)
int_list = list(map(lambda x : int(x),str_list))
print(int_list)
print("합계 :", sum(int_list))