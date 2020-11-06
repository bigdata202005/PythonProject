# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return을 이용한 방법
def plusOne(a):
    return a + 1

a = 10;
print("main에서 호출전 a = {}".format(a))
a = plusOne(a)  # 리턴값을 자신의 변수로 받는다.
print("main에서 호출후 a = {}".format(a))


# global 키워드 사용방법
def plusOne2():
    global a
    a += 1

print("main에서 호출전 a = {}".format(a))
plusOne2()
print("main에서 호출후 a = {}".format(a))

