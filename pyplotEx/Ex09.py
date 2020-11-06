# Ex09.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 축 범위 지정하기
matplotlib.pyplot 모듈의 axis() 함수를 사용하면 x, y 축이 표시되는 범위를 지정할 수 있습니다.
axis() 함수에 [xmin, xmax, ymin, ymax]의 형태로 x, y 축의 범위를 지정해줍니다.
입력 리스트는 반드시 네 개의 값 (xmin, xmax, ymin, ymax)이 있어야 합니다.
입력값이 없으면 데이터에 맞게 자동으로 범위를 지정합니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
print(plt.rcParams['font.family'])
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')

array1 = np.linspace(1, 10, 10)
array2 = np.linspace(1, 20, 10)
# 축 범위 지정하기 :  (xmin, xmax, ymin, ymax)
plt.axis([0, 10, 0, 20])

plt.plot(array1, array2, 'gs')  # 녹색 사각점 그래프
plt.show()
