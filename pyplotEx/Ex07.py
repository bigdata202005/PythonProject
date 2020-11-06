# Ex07.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 축 레이블 설정하기
matplotlib.pyplot 모듈의 xlabel(), ylabel() 함수를 사용하면 
그래프의 x, y 축에 대한 레이블을 표시할 수 있습니다.
"""
array1 = np.linspace(1, 10, 10)
array2 = np.linspace(1, 20, 10)
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.plot(array1, array2, 'gs')  # 녹색 사각점 그래프
plt.show()
