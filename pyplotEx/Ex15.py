# Ex15.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 그래프 영역 채우기 1
그래프의 특정 영역을 색상으로 채워서 강조할 수 있습니다.
matplotlib.pyplot 모듈에서 그래프의 영역을 채우는 세가지 함수
fill_between()
fill_betweenx()
fill()

fill_between() 함수에 x[1:3], y[1:3]를 순서대로 입력하면,
네 점 (x[1], y[1]), (x[2], y[2]), (x[1], 0), (x[2], 0)을 잇는 영역이 채워집니다.

fill_betweenx() 함수에 y[2:4], x[2:4]를 순서대로 입력하면,
네 점 (x[2], y[2]), (x[3], y[3]), (0, y[2]), (0, y[3])을 잇는 영역이 채워집니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
print(plt.rcParams['font.family'])
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, 'r*')

plt.fill_between(x[1:3], y[1:3], alpha=0.5)                 ## fill_between() 사용
plt.fill_betweenx(y[2:4], x[2:4], color='pink', alpha=0.5)  ## fill_betweenx() 사용

plt.show()
