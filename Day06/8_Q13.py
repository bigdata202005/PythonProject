"""
Q13 DashInsert 함수
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤
문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
DashInsert 함수를 완성하시오.

입력 예시: 4546793
출력 예시: 454*67-9-3
"""


def DashInsert(num):
    str_num = str(num)
    result_num = str_num[0]
    for i in range(1, len(str_num)):
        # print(i, " :", str_num[i-1], " :", str_num[i])
        if int(str_num[i - 1]) % 2 == 0 and int(str_num[i]) % 2 == 0:
            result_num += "*"
        elif int(str_num[i - 1]) % 2 != 0 and int(str_num[i]) % 2 != 0:
            result_num += "-"
        result_num += str_num[i]
    return result_num


print(DashInsert(4546793))
