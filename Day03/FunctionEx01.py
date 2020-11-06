def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def sqrt(a, b):
    return a ** b


def mod(a, b):
    return a % b


a = 10
b = 3
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
print("{} % {} = {}".format(a, b, mod(a, b)))
print("{} ** {} = {}".format(a, b, sqrt(a, b)))
