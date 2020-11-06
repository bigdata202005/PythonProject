# Ex20.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 그리드 설정하기 2
축 지정하기
axis=y로 설정하면 가로 방향의 그리드만 표시됩니다.
{‘both’, ‘x’, ‘y’} 중 선택할 수 있고 디폴트는 ‘both’입니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
a = np.arange(0, 2, 0.2)
plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')
# 축의 범위 [xmin, xmax, ymin, ymax]를 지정
plt.axis([0, 2, 0, 2])
# 그리드 설정
plt.grid(True, axis='x')
plt.show()

plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')
# 축의 범위 [xmin, xmax, ymin, ymax]를 지정
plt.axis([0, 2, 0, 2])
# 그리드 설정
plt.grid(True, axis='y')
plt.show()

plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')
# 축의 범위 [xmin, xmax, ymin, ymax]를 지정
plt.axis([0, 2, 0, 2])
# 그리드 설정
plt.grid(True, axis='both')
plt.show()
