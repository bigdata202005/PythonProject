# Ex05.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib y 값 입력하기
Matplotlib에서는 일반적으로 NumPy 어레이를 이용
하나의 리스트로 값들을 입력하면 y 값으로 인식합니다.
x 값은 자동으로 생성되는 값인 [0, 1, 2, 3...이 되어서 점 (0, 1), (1, 2), (2, 3), ...를 잇는 
그래프가 나타납니다.
"""
plt.plot(np.arange(1, 10), 'bo')  # 파란색 원형점 그래프
plt.show()
