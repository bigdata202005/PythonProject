# print(5/0) # ZeroDivisionError: division by zero

try:
    first = int(input('첫번째 정수 입력 :'))
    second = int(input('두번째 정수 입력 :'))
    result = first / second
    print("{} 나누기 {}의 결과는 {}".format(first, second, result))
except ZeroDivisionError as e:
    print("예외발생 :", e)

