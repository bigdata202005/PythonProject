# 프로그램을 만들려면 가장 먼저 "입력"과 "출력"을 생각하라.
# 함수 이름은? GuGu로 짓자
# 입력받는 값은? 2
# 출력하는 값은? 2단(2, 4, 6, 8, …, 18)
# 결과는 어떤 형태로 저장하지? 연속된 자료형이니까 리스트!

def GuGu(dan):
    result = list()
    for i in range(1, 10):
        result.append(dan * i)
    return result


result = GuGu(3)
print(result)
for i in range(1,10):
    print("{:02d}단".format(i), GuGu(i))