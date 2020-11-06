# Ex08.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 축 레이블 설정하기
matplotlib.pyplot 모듈의 xlabel(), ylabel() 함수를 사용하면 
그래프의 x, y 축에 대한 레이블을 표시할 수 있습니다.
suptitle(제목) : 그래프의 제목 지정
gcf().canvas.set_window_title(제목) : 윈도우의 제목 지정
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
plt.plot(array1, array2, 'gs')  # 녹색 사각점 그래프
plt.show()
