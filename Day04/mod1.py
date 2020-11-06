# mod1.py
def add(a, b):
    return a + b


def sub(a, b):
    return a-b


# 모듈 작성시 테스트용 코드를 썼다!!!!
# 이 모듈을 import하면 실행이 된다.
# 이렇게 되면 테스트가 끝나고 다음의 코드들을 지워줘야 한다!!!
# 이럴때 main을 사용한다.
# __main__은 단독으로 실행될때만 작동한다.
if __name__ == "__main__":
    print(__name__)
    print(add(1, 4))
    print(sub(4, 2))

