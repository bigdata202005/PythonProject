# Ex13.py
import numpy as np
import matplotlib.pyplot as plt

"""
Matplotlib 색상 지정하기3
Hex code 사용하기
16진수 코드 (Hex code) 로 더욱 다양한 색상을 지정할 수 있습니다.
이번에는 선의 색상과 함께 마커와 선의 종류까지 모두 지정해 보겠습니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
print(plt.rcParams['font.family'])
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
array = np.linspace(0, 2, 10)
# print(array)
# 16진수 색상값으로 지정
plt.plot(array, array, color='#E35F62', marker=">", linestyle='--' )
plt.plot(array, array**2, color='#AA5F88', marker="*", linestyle='-' )
plt.plot(array, array**3, color='#009962', marker="^", linestyle='-.' )
plt.show()
