# Ex18.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 여러 곡선 그리기
plot() 함수에 x 값, y 값, 스타일을 순서대로 세 번씩 입력하면, 세 개의 곡선 (y=x, y=x^2, y=x^3)이 동시에 그려집니다.
‘r–‘은 빨간색 (Red)의 대쉬 (Dashed) 스타일 선,
‘bo’는 파란색 (Blue)의 원형 (Circle) 마커,
‘g-.’은 녹색 (Green)의 대쉬-닷 (Dash-dot) 스타일 선을 의미합니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
a = np.arange(0, 2, 0.2)
plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')
plt.show()
