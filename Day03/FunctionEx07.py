# 리턴값의 개수?
def add_mul(a, b):
    return a + b, a * b


result = add_mul(11, 22)
print(type(result))
print(result)

a, b = add_mul(5, 6)
print(a)
print(b)


# 자연수 1개를 넘기면 그 수의 1승~ 10승까지를 리스트로 리턴해주는 함수
def power(n):
    return [n ** i for i in range(1, 11)]


power2 = power(2)
print(type(power2))
print(power2)

print(power(3))
