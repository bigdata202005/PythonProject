import datetime     # 날짜와 시간을 지원하는 모듈

# 멤버가 __로 시작하면 private이고 기본적으로 public이다.
class MyDate:
    def __init__(self):
        now = datetime.datetime.now()   # 현재 시간
        self.__yy = now.year
        self.__mm = now.month
        self.__dd = now.day
        self.__hour = now.hour
        self.__minute = now.minute
        self.__second = now.second

    def __makeStr(self):
        return "{}년 {}월 {}일 {}시 {}분 {}초".format(self.__yy, self.__mm, self.__dd,
                                                self.__hour, self.__minute, self.__second)

    def __str__(self):
        return self.__makeStr()


today = MyDate()
print(today)
print(vars(today))
print(dir(today))
# print(today.__makeStr()) # 에러 : AttributeError: 'MyDate' object has no attribute '__makeStr'
# print(today.__yy) # 에러 : AttributeError: 'MyDate' object has no attribute '__yy'
