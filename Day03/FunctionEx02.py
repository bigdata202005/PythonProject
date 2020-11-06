# 인수도 없고 리턴도 없다
def line():
    print('_' * 80)

# 함수의 호출
line()


# 같은 이름을 사용하면 기존 함수가 지워진다.
def line(count):
    print('_' * count)


# line()  # TypeError: line() missing 1 required positional argument: 'count' !!! 오버로딩 않됨
line(40)

print(len('1234567890'))
len = 33  # 파이선의 함수도 재정의 된다!!!
print(len('1234567890'))  # TypeError: 'int' object is not callable : len이란 함수 없어!!!

