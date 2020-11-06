# Ex11.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 색상 지정하기1
plot() 함수에 아래와 같이 입력하면 각각 빨간색, 파란색, 녹색 선의 그래프가 그려집니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
print(plt.rcParams['font.family'])
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
array = np.linspace(0, 2, 100)
# print(array)
# 기본 색상값으로 지정
plt.plot(array, array, 'r')
plt.plot(array, array**2, 'g')
plt.plot(array, array**3, 'b')
plt.show()
