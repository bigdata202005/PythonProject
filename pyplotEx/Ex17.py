# Ex17.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 그래프 영역 채우기 3
임의의 영역 채우기
fill() 함수에 x, y 값의 리스트를 입력해주면,
각 x, y 점들로 정의되는 다각형 영역을 자유롭게 지정해서 채울 수 있습니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.fill([1.9, 1.9, 3.1, 3.1], [2, 5, 11, 8], color='lightgray', alpha=0.5)
plt.show()

