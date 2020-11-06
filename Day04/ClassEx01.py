result = 0


def add(num):
    global result
    result += num
    return result


print(add(3))
print(add(4))
print(result)   # result가 전역이기 때문에 아무곳에서나 사용 가능
result = 100    # 전역변수의 문제점은 아무곳에서나 수정이 가능하다.  위험하다.
print(add(4))   # 3+4+4 = 11 이기를 바랬지만 104가 나온다. 함수에 이해서만 변경되어야 하는데\
                # 전역변수 여서 값이 외부에서 함부로 변경되었다.



