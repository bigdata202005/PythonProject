# Ex12.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 색상 지정하기2
plot() 함수에 아래와 같이 CSS 색상값을 입력하면 각각 지정 색상의 선 그래프가 그려집니다.
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
# css색상값으로 지정
plt.plot(array, array, 'springgreen')
plt.plot(array, array**2, 'violet')
plt.plot(array, array**3, 'teal')
plt.show()
