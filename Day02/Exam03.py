# Lunar Arithmetic
# Lunar(Dismal) Arithmetic 라는 어떤 연산이 있습니다.
# 이 연산에서 덧셈「+」은 각 자릿수를 비교해서 큰 수를 취합니다.
# 5 + 3 = 5
# 13 + 6 = 16
#    169
#  + 248
#  ------
#    269
# 그리고 곱셈「×」은 각 자릿수를 비교해서 작은 수를 취합니다.
#
# 5 × 3 = 3
# 13 × 6 = 13
#
#      169
#    × 248
#    ------
#      168
#     144
#  + 122
#  --------
#    12468
# Lunar Arithmetic를 수행하는 계산기를 만들어봅시다.

def dismal_add(n, m):
    # print(len(str(n)))
    # print(len(str(m)))
    # max_length = len(str(n)) if len(str(n)) > len(str(m)) else len(str(m))
    # print(max_length)
    max_length = max(len(str(n)), len(str(m)))
    # print(max_length)
    str_n = str(n).zfill(max_length)
    str_m = str(m).zfill(max_length)
    # print(str_n, str_m)
    # for i in range(max_length):
    #   print(str_n[i], str_m[i], max(str_n[i], str_m[i]))
    result = [max(str_n[i], str_m[i]) for i in range(max_length)]
    print(int("".join(result)))


def dismal_add2(n, m):
    n, m = str(n)[::-1], str(m)[::-1]  # 문자열 뒤집기
    #for i in range(max(len(n), len(m))):
    #    print(n[i:i + 1], m[i:i + 1], max(n[i:i + 1], m[i:i + 1]))
    print(int("".join([max(n[i:i + 1], m[i:i + 1]) for i in range(max(len(n), len(m)))])))


dismal_add2(1234, 24)
dismal_add2(5, 3)
dismal_add2(13, 6)
dismal_add2(169, 248)

"""
dismal_add(1234, 24)
dismal_add(5, 3)
dismal_add(13, 6)
dismal_add(169, 248)
"""
