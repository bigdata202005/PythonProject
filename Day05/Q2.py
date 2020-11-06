# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는
# MaxLimitCalculator 클래스를 만들어 보자. 즉 다음과 같이 동작해야 한다.
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator (Calculator):
    # 오버라이딩
    def add(self, val):
        self.value += val
        # 값이 100이상이면 100을 가지게 한다.
        if self.value>100:
            self.value = 100


if __name__ == '__main__':
    cal = MaxLimitCalculator()
    cal.add(50)  # 50 더하기
    cal.add(60)  # 60 더하기

    print(cal.value)  # 100 출력