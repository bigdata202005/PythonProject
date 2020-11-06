# 클래스 선언
class Calculator:
    # 생성자
    def __init__(self):
        self.result = 0     # 변수 선언

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()  # 객체 선언
cal2 = Calculator()  # 객체 선언

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

cal1.result = 100   # 변수도 전역이다!!!
print(cal1.add(4))
print(cal2.add(4))  # 객체마다 따로 변수가 저장된다.

