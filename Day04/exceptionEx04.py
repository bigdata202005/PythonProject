try:
    a = [1, 2]
    print(a[3])  # IndexError
    4/0 # ZeroDivisionError
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


try:
    a = [1, 2]
    4/0
    print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)
