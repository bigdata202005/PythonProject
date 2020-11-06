"""
Q15 Duplicate Numbers
0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
출력 예시: true false false true false
"""


def DuplicateNumbers(number):
    for i in range(0, 10):
        # print(i, " :", number.count(str(i)))
        if number.count(str(i)) != 1:
            return False
    return True


def DuplicateNumbers2(number):
    # print("".join(sorted(number)))
    return "".join(sorted(number)) == "0123456789"


print(DuplicateNumbers("0123456789"), end=" ")
print(DuplicateNumbers("01234"), end=" ")
print(DuplicateNumbers("01234567890"), end=" ")
print(DuplicateNumbers("6789012345"), end=" ")
print(DuplicateNumbers("012322456789"))
print('-' * 80)

print(DuplicateNumbers2("0123456789"), end=" ")
print(DuplicateNumbers2("01234"), end=" ")
print(DuplicateNumbers2("01234567890"), end=" ")
print(DuplicateNumbers2("6789012345"), end=" ")
print(DuplicateNumbers2("012322456789"))
print('-' * 80)

DuplicateNumbers3 = lambda x: "".join(sorted(x)) == "0123456789"
print(DuplicateNumbers3("0123456789"), end=" ")
print(DuplicateNumbers3("01234"), end=" ")
print(DuplicateNumbers3("01234567890"), end=" ")
print(DuplicateNumbers3("6789012345"), end=" ")
print(DuplicateNumbers3("012322456789"))
print('-' * 80)
