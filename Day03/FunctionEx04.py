# 함수가 기본인수값을 가질 수 있다. 그래서 오버로딩의 효과를 볼 수 있다
def line(count=80, char='_'):
    print(char * count)


def line2(count, char='&'):
    print(char * count)

# 기본 값을 줄때는 뒤에서 부터 줘야 한다.
# def line3(count=50, char, cnt = 7):
#    print(char * count)


# line2()  # TypeError: line2() missing 1 required positional argument: 'count'
line2(40, '_')
line2(40)

line()
line(60)
line(5, "^_")
line(50, '~')
line('~', 40)
line(count=50, char='^')
line(char='*', count=20)

