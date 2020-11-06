# 스레드 : 실행흐름이 여러개인 프로그램
# 다음은 스레드가 아닌 순차적 실행인 프로그램이다
import time


def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("실행 : {}회".format(i+1))


print("시작!!!")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("종료!!!")