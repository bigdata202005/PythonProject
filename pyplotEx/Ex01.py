# Ex01.py
import matplotlib.pyplot as plt
"""
yplot.plot() 함수에 하나의 숫자 리스트를 입력함으로써 아래와 같은 그래프가 그려집니다.
Matplotlib은 리스트의 값들이 y 값들이라고 가정하고, x 값 [0, 1, 2, 3]을 자동으로 만들어냅니다.
"""
plt.plot([1, 2, 3, 4])
plt.ylabel('y-label')
plt.show()