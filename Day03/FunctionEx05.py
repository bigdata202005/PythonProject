# 가변 인수 : 인수의 개수가 정해져있지 않다
def sum_all(*args):
    print(type(args))
    s = 0
    for n in args:
        s += n
    return s


print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(sum_all(1, 2, 3))
# print(sum_all([11, 22, 33]))
# print(sum_all((11, 22, 33)))
