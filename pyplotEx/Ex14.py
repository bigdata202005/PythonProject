# Ex14.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 색상 지정하기4
합성해서 한번에 선의 색상과 함께 마커와 선의 종류 그리고 법례까지 모두 지정해 보겠습니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
print(plt.rcParams['font.family'])
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
array = np.linspace(0, 2, 10)
# print(array)
# 합성해서 한번에 지정
plt.plot(array, array, 'r^-.', label='범례1')
plt.plot(array, array**2, 'b>-', label='범례2')
plt.plot(array, array**3, 'c*--', label='범례3')
plt.legend() # 범례를 표시해라!!!
plt.show()
