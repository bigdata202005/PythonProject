# 함수 안에서 선언한 변수의 효력 범위
def vartest(a):
    b = a + 100
    print("vartest 에서 변경전 a = {}".format(a))
    a += 10  # a는 함수 안에서마 유효하다
    print("vartest 에서 변경후 a = {}".format(a))


a = 100
print("main에서 호출전 a = {}".format(a))
vartest(a)
print("main에서 호출후 a = {}".format(a))

# print("main에서 b 호출 b = {}".format(b))  # NameError: name 'b' is not defined


