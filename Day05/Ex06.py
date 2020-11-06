# time
# 시간과 관련된 time 모듈에는 함수가 굉장히 많다.
import time
print(time.time())
print(time.localtime(time.time()))
today = time.localtime(time.time())
print(type(today))
# print(str(today.tm_year) + "년 ")
print("{}년 {}월 {}일".format(today.tm_year,today.tm_mon,today.tm_mday))
print("{}시 {}분 {}초".format(today.tm_hour,today.tm_min,today.tm_sec))

print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.clock())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

# 일정시간 대기
time.sleep(5)
print("5초후 내용이 보임!!!")