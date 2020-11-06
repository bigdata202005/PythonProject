# Ex10.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 마커 지정하기
특별한 입력이 없으면 그래프가 실선으로 그려지지만, 마커 형태를 지정하여 그래프를 그릴 수 있습니다.
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
# 축 범위 지정하기 :  (xmin, xmax, ymin, ymax)
plt.axis([0, 10, 0, 20])
# 이미지(maker.png) 참조
plt.plot(array1, array2, 'k*')  # 검정 별점 그래프
plt.show()
