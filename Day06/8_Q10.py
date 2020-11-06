"""
Q10 사칙연산 계산기
다음과 같이 동작하는 클래스 Calculator를 작성하시오.

cal1 = Calculator([1,2,3,4,5])
cal1.sum() # 합계
15
cal1.avg() # 평균
3.0
cal2 = Calculator([6,7,8,9,10])
cal2.sum() # 합계
40
cal2.avg() # 평균
8.0
"""


class Calculator:
    def __init__(self, data_list):
        self.data_list = data_list

    def sum(self):
        print(sum(self.data_list))

    def avg(self):
        print(round(sum(self.data_list) / len(self.data_list), 1))


if __name__ == '__main__':
    cal1 = Calculator([1, 2, 3, 4, 5])
    cal1.sum()  # 합계
    cal1.avg()  # 평균
    cal2 = Calculator([6, 7, 8, 9, 10])
    cal2.sum()  # 합계
    cal2.avg()  # 평균