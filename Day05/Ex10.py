# 스레드 : 실행흐름이 여러개인 프로그램
# 다음은 스레드 프로그램이다
import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def print_num():
    for i in range(1,27):
        time.sleep(1)
        print(i, sep=' ', end=' ')

def print_alphabet():
    for i in tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        time.sleep(1)
        print(i, sep=' ', end=' ')



print("시작!!!")

threads = [threading.Thread(target=print_num),threading.Thread(target=print_alphabet), ]

for t in threads:
    t.start()  # 스레드를 실행한다

print("종료!!!")