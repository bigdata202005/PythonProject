# 고급 인덱싱 및 인덱스 트릭
# 배열은 정수 배열과 부울 배열로 인덱싱 할 수 있습니다.
import numpy as np

# 배열을 사용한 인덱싱의 또 다른 일반적인 용도는
# 시간 종속 계열의 최대 값을 검색하는 것입니다.
time = np.linspace(20, 145, 5)                 # time scale
data = np.sin(np.arange(20)).reshape(5, 4)      # 4 time-dependent series
print("time배열")
print(time)
print("data배열")
print(data)
print("~" * 80)

# argmax(axis=축값) : 축을 따라 최대 값의 인덱스를 반환합니다.
ind = data.argmax(axis=0)  # 열의 최대값 인덱스 배열
print(ind)
print("~" * 80)

time_max = time[ind]
# => data[ind[0],0], data[ind[1],1]...
data_max = data[ind, range(data.shape[1])]
print(data.shape)       # 행열의 크기를 튜플로
print(data.shape[0])    # 행
print(data.shape[1])    # 열
print(time_max)
print(data_max)
print("~" * 80)


print(np.all(data_max == data.max(axis=0)))