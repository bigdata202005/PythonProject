# Ex22.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 수직선/수평선 표시하기
그래프의 특정 값에 해당하는 위치에 수직선/수평선을 표시하기 위해서
matplotlib.pyplot 모듈에서는 아래의 네가지 함수를 지원합니다.
axhline()
axvline()
hlines()
vlines()

axhline() 함수의 첫번째 인자는 y 값으로서 수평선의 위치가 됩니다.
두, 세번째 인자는 xmin, xmax 값으로서 0에서 1 사이의 값을 입력합니다.
0은 왼쪽 끝 (y축), 1은 오른쪽 끝을 의미합니다.

axvline() 함수의 첫번째 인자는 x 값으로서 수직선의 위치가 됩니다.
두, 세번째 인자는 ymin, ymax 값으로서 0에서 1 사이의 값을 입력합니다.
0은 아래쪽 끝 (x축), 1은 위쪽 끝을 의미합니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
a = np.arange(0, 4, 0.2)
plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')

plt.axhline(1, 0, 0.55, color='red', linestyle='--', linewidth='1')
plt.axvline(1, 0, 0.16, color='red', linestyle=':', linewidth='2')

plt.axhline(5.83, 0, 0.95, color='blue', linestyle='--', linewidth='1')
plt.axvline(1.8, 0, 0.95, color='blue', linestyle=':', linewidth='2')
plt.show()


a = np.arange(0, 2, 0.2)

plt.plot(a, a, 'bo')
plt.plot(a, a**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(a, a**3, color='springgreen', marker='^', markersize=9)
"""
hlines() 함수에 y, xmin, xmax를 순서대로 입력하면, 점 (xmin, y)에서 점 (xmax, y)를 따라 수평선을 표시합니다.
vlines() 함수에 x, ymin, ymax를 순서대로 입력하면, 점 (x, ymin)에서 점 (x, ymax)를 따라 수평선을 표시합니다.
"""
plt.hlines(4, 1, 1.6, colors='pink', linewidth=3)
plt.vlines(1, 1, 4, colors='pink', linewidth=3)
plt.show()