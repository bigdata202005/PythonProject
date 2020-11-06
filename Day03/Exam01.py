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
    max_length = max(len(str(n)), len(str(m)))
    str_n = str(n).zfill(max_length)
    str_m = str(m).zfill(max_length)
    result = [max(str_n[i], str_m[i]) for i in range(max_length)]
    return int("".join(result))


def dismal_mul(n, m):
    cnt = 0
    list1 = []
    for i in str(m)[::-1]:
        c = "";
        for j in str(n)[::-1]:
            c = min(i, j) + c
        c += "0" * cnt
        cnt += 1
        list1.append(c)
    result = 0
    for data in list1:
        result = dismal_add(result, data)
    return result;


print(dismal_mul(5, 3))
print(dismal_mul(13, 6))
print(dismal_mul(169, 248))
print("*" * 50)

print(dismal_add(1234, 24))
print(dismal_add(5, 3))
print(dismal_add(13, 6))
print(dismal_add(169, 248))
print("*" * 50)

