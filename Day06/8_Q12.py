"""
Q12 오류와 예외 처리
다음 코드의 실행 결과를 예측하고 그 이유에 대해 설명하시오.

result = 0

try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
"""
result = 0

try:
    [1, 2, 3][3]  # 여기서 에러 : IndexError  ---- 1
    "a"+1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3  # +3           ---- 2
finally:  # 여기는 무조건 실행
    result += 4  # +4           ---- 3

print(result)  # 7              ---- 4
