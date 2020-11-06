# 스레드 : 실행흐름이 여러개인 프로그램
# 다음은 스레드 프로그램이다
import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("실행 : {}회".format(i+1))


print("시작!!!")

threads = list()
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t) # 리스트에 스레드 추가

for t in threads:
    t.start()  # 스레드를 실행한다

print("종료!!!")