try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass  # 예외 피하기


# 예외 발생하기
class Bird:
    def fly(self):
        raise NotImplementedError  # 예외발생


class Eagle(Bird):
    def fly(self): # 재정의
        print("very fast")


try:
    bird = Bird()
    print(bird.fly())
except NotImplementedError as e:
    print("예외발생!!!!", e)

eagle = Eagle()
eagle.fly()
