"""
Q14 문자열 압축하기
문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에
그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.

입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
"""


def zip_string(zip_str):
    result = zip_str[0]
    old_str = zip_str[0]
    count = 0
    for c in zip_str:
        if c == old_str:  # 이전 글자와 같으면 개수 증가하고 계속
            count += 1
            continue
        else: # 이전 글자와 다르면 숫자와 현재문자 더하고 변수 초기화
            result += str(count) + c
            count = 1
            old_str = c
    result += str(count)  # 마지막에 숫자
    return result

# 입력 예시: aaabbcccccca
# 출력 예시: a3b2c6a1
print(zip_string("aaabbcccccca"))
print(zip_string("Aaaabbccccccaass"))

