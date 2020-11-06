# mod2.py
# 상수
PI = 3.141592

# 클래스
class Math:
    def solv(self, r):
        return PI * (r ** 2)

# 함수
def add(a, b):
    return a + b


if __name__ == '__main__':
    print("원주율 :", PI)
    math = Math()
    print("반지름 7인 원의 넓이 :", math.solv(r=7))
    print("{} + {} = {}".format(5, 8, add(5, 8)))
