# Ex04.py

import numpy as np
import matplotlib.pyplot as plt
"""
여러 개의 그래프 그리기
Matplotlib에서는 일반적으로 NumPy 어레이를 이용하게 되는데,
사실 NumPy 어레이를 사용하지 않더라도 모든 시퀀스는 내부적으로 NumPy 어레이로 변환됩니다.
아래의 예제는 다양한 스타일을 갖는 여러 개의 곡선을 하나의 그래프로 나타냅니다.
"""
# 200ms 간격으로 균일하게 샘플된 시간
t = np.arange(0., 5., 0.2)
# 빨간 대쉬, 파란 사각형, 녹색 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()