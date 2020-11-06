# Ex23.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 눈금에 값 표시하기
xticks
yticks
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
a = np.arange(0, 2, 0.2)

plt.plot(a, a, 'bo')
plt.plot(a, a**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(a, a**3, color='springgreen', marker='^', markersize=9)
# 눈금에 값표시
plt.xticks(np.arange(0, 2, 0.2), labels=['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월'])
plt.yticks(np.arange(0, 7), ('0', '1GB', '2GB', '3GB', '4GB', '5GB', '6GB'))

plt.show()

plt.plot(a, a, 'bo')
plt.plot(a, a**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(a, a**3, color='springgreen', marker='^', markersize=9)
# 눈금에 값표시
plt.xticks(np.arange(0, 2, 0.2), labels=['1월', '', '3월', '', '5월', '', '7월', '', '9월', ''])
plt.yticks(np.arange(0, 7), ('0', '1GB', '', '3GB', '4GB', '', '6GB'))
plt.show()