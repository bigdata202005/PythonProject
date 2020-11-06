# Ex06.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib x, y 값 입력하기
Matplotlib에서는 일반적으로 NumPy 어레이를 이용
두개의 리스트로 값들을 입력하면 x, y 값으로 인식합니다.
"""
array1 = np.linspace(1, 10, 10)
array2 = np.linspace(1, 20, 10)
print(array1)
print(array2)
plt.plot(array1, array2, 'gs')  # 녹색 사각점 그래프
plt.show()
