# 내장함수 : 파이선에 이미 등록되어 있는 함수로 아무런 조치 없이 바로 사용 가능한 함수
# abs : 절대값(0으로 부터 얼마만큼 떨어져 있느냐?)
print(abs(3))
print(abs(-33))
print(abs(-1.3))

# all
# all(x)는 반복 가능한(iterable) 자료형
# x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))  # all의 입력 인수가 빈 값인 경우에는 True를 리턴한다.
print()
# any
# any(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이
# x의 요소 중 하나라도 참이 있으면 True를 돌려주고,
# x가 모두 거짓일 때에만 False를 돌려준다. all(x)의 반대이다.
print(any([1, 2, 3]))
print(any([1, 2, 3, 0]))
print(any([]))  # 만약 any의 입력 인수가 빈 값인 경우에는 False를 리턴한다.
print()

# chr
# chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다.
print(chr(97))
print(chr(65))
print(chr(48))
print()

# dir
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
print(dir([1, 2, 3]))
print()

# divmod : 몫과 나머지를 튜플로 반환
print(divmod(10, 3))
print()

# enumerate
# enumerate는 "열거하다"라는 뜻이다.
# 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을
# 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print()

for index, value in enumerate(['body', 'foo', 'bar']):
    print(index, value)
print()

# eval
# eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아
# 문자열을 실행한 결괏값을 돌려주는 함수이다.
print('1+2')
print(eval('1+2'))

print('divmod(4, 3)')
print(eval('divmod(4, 3)'))
print()


# filter
# filter란 무엇인가를 걸러낸다는 뜻으로 filter 함수도 동일한 의미를 가진다.
def positive1(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result


print(positive1([1, -3, 2, 0, -5, 6]))
print()


def positive2(x):
    return x > 0


print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))
print()

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# hex
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
print(hex(123))
for i in range(1, 21):
    print(hex(i))

# id
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 4
b = a
print(id(a))
print(id(4))
print(id(b))
a = 8
print(a, b)
print(id(a))
print(id(8))
print(id(b))
print()


# isinstance
# isinstance(object, class )는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

class Some:
    pass


a = Some()
print(isinstance(a, Some))
b = 123
print(isinstance(b, Some))
print()

# len
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
print(len('qwerty'))
print(len([1, 2, 3]))
print(len((1, 2)))
print(len({'name': 'kimc'}))


# map
# map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
# map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.


def two_times1(numberList):
    """리스트의 값을 두배로 변경하여 리턴"""
    result = []
    for number in numberList:
        result.append(number * 2)
    return result


result = two_times1([1, 2, 3, 4])
print(result)


def two_times2(x):
    return x * 2


print(list(map(two_times2, [1, 2, 3, 4, 5])))

print(list(map(lambda x : x * 2, [1, 2, 3, 4, 5])))

print(max([4,3,2,1,6]))
print(max("pythonPYTHON한글"))
print(min([4,3,2,1,6]))
print(min("pythonPYTHON한글"))
print()

# 각각의 진법표현
for i in range(1,21):
    print(i, hex(i), oct(i), bin(i))  # 10진수, 16진수, 8진수, 2진수
print()

# chr, ord
print(chr(65), ord('A'), chr(ord('A')))
print()

# pow : pow(x, y)는 x의 y 제곱한 결괏값을 돌려주는 함수이다.
print(pow(2,10), 2**10)
print()

# range
# range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다.
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.

a = range(1,10)  # 버전2에서는 타입이 list였다
print(type(a))   # <class 'range'> 3에서는 range타입
print(a)
print(list(a))
print(list(range(10)))
print(list(range(0, 10, 1)))
print(list(range(0, 10, 3)))
print(list(range(0, -10, -1)))


# round
# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
print(3.14, " :", round(3.14))
print(-3.14, " :", round(-3.14))
print(round(5.67890, 1))
print(round(5.67890, 2))
print(round(5.67890, 3))
print(round(5678.9876, -2)) # 음수를 쓰면 양의 자리에서 처리!!!

# sorted
# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("Python 재미없다!"))

# sum
# sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
print(sum([1,2,3]))
print(sum((1,2,3)))
print()

# tuple
# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다.
# 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
print(tuple('Python'))
print(tuple('1234567890'))
print(tuple('갑을병전무기경신임계'))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

# 문제 : 60갑자를 출력해보시오!!!! 갑자, 을축....
gan = tuple('갑을병전무기경신임계')
ji = tuple('자축인묘진사오미신유술해')
print(gan[0] + ji[0])
print('-' * 80)
for i in range(60):
    print(gan[i%10] + ji[i%12], end=" ")
    if (i+1)%12 ==0:
        print()
print('-' * 80)

# zip
# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip((1, 2, 3), [4, 5, 6])))
print(list(zip('123', '일이삼')))
print(list(zip('123', '일이')))
print('-' * 80)


