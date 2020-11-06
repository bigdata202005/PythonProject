# 1~ n까지의 합을 구하는 함수 작성
def sum1(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s


# n!을 구하는 함수 작성
def fac(n):
    f = 1
    for i in reversed(range(1, n+1)):
        f *= i
    return f


# n ~ m까지의 합을 구하는 함수 작성
def sum2(n, m):
    s = 0
    """
    n = min(n, m)
    m = max(n, m)
    """
    n, m = min(n, m), max(n, m)
    for i in range(n, m+1):
        s += i
    return s


print("1~100까지의 합 : ", sum1(100))
print("5! = ", fac(5))
print("1~100까지의 합 : ", sum2(100, 1))
print("1~100까지의 합 : ", sum2(1, 100))


for i in range(1, 11):
    print(i)
print("*" * 50)

for i in range(10, 0):
    print(i)
print("*" * 50)

for i in reversed(range(1, 11)):
    print(i)
print("*" * 50)

