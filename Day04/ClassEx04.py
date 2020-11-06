class FourCal:
    def __init__(self):
        self.a = 0
        self.b = 0

    def setData(self, a, b):
        self.a = a
        self.b = b

    def getData(self):
        return self.a, self.b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def mod(self):
        return self.a % self.b


# 상속 : 부모클래스(자식클래스)
class MoreFourCal(FourCal):
    def __init__(self):
        pass

    def __init__(self, a, b):  # 함수의 재정의가 되어 위의 생성자는 사라진다.
        self.a = a
        self.b = b

    def power(self):
        return self.a ** self.b  # 부모의 변수 사용 가능

    def div(self):   # 함수의 재정의가 되어 부모의 함수는 사라진다.
        return self.a // self.b


calc1 = FourCal()
calc1.setData(4, 5)
print(calc1.getData())
print(calc1.add())
print(calc1.sub())
print(calc1.mul())
print(calc1.div())
print(calc1.mod())

# calc2 = MoreFourCal()  에러!!!
# calc2.setData(2, 10)

calc2 = MoreFourCal(2,10)
print(calc2.getData())
print(calc2.add())
print(calc2.sub())
print(calc2.mul())
print(calc2.div())
print(calc2.mod())
print(calc2.power())


class SafeFourCal(FourCal):
    def div(self):
        if self.b == 0:  # 나누는 값이 0이면 ZeroDivisionError: division by zero 에러 발생!!!
            return 0
        else:
            return self.a / self.b


calc3 = SafeFourCal()
calc3.setData(5, 0)
print(calc3.div())
