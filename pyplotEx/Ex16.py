# Ex16.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 그래프 영역 채우기 2
두 개의 그래프 커브 사이 영역을 채우기 위해서는 두 개의 y 값 시퀀스 y1, y2를 입력해줍니다.
네 점 (x[1], y[1]), (x[1], y[2]), (x[2], y[1]), (x[2], y[2]) 사이 영역을 채웁니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
print(plt.rcParams['font.family'])
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.fill_between(x[1:3], y1[1:3], y2[1:3], color='lightgray', alpha=0.5)

plt.show()
