# Ex21.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 그리드 설정하기 3
color, alpha, linestyle 파마리터를 사용해서 그리드 선의 스타일을 설정했습니다.
또한 which 파라미터를 ‘major’, ‘minor’, ‘both’ 등으로 사용하면 
주눈금, 보조눈금에 각각 그리드를 표시할 수 있습니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
a = np.arange(0, 4, 0.2)
plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')
# 축의 범위 [xmin, xmax, ymin, ymax]를 지정
plt.axis([0, 4, 0, 4])
# 그리드 설정
plt.grid(True, axis='both',  color='red', alpha=0.5, linestyle='--')
plt.show()

plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')
# 축의 범위 [xmin, xmax, ymin, ymax]를 지정
plt.axis([0, 4, 0, 4])
plt.grid(True, axis='both',  color='blue', alpha=0.3, linestyle='-.', which='major')
plt.show()

plt.plot(a, a, 'r--', a, a**2, 'bo', a, a**3, 'g-.')
# 축의 범위 [xmin, xmax, ymin, ymax]를 지정
plt.axis([0, 4, 0, 4])
plt.grid(True, axis='both',  color='green', alpha=0.7, linestyle='-.', which='minor')
plt.show()

