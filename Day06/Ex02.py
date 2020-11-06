# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.


# 1. 합계를 저장할 변수
# 2. 1 ~ 1000까지 반복
# 3. 3의배수 또는 5의배수를 판단

def my_sum(limit):
    sum = 0
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    print("1~10미만 3과 5의 배수 합 :", my_sum(10))
    print("1~1000미만 3과 5의 배수 합 :", my_sum(1000))
