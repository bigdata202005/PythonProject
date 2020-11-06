# print(5/0) # ZeroDivisionError: division by zero

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

