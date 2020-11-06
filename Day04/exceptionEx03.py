# print(5/0) # ZeroDivisionError: division by zero
file = None
try:
    file = open("test.txt", "r", encoding='utf8')
    data = file.read()
    print(data)
except FileNotFoundError as e:
    print("예외발생!!!")
finally:
    print("실행될까!!!!")
    if file is not None:
        file.close()




