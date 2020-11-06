# Ex24.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 막대 그래프 그리기
막대 그래프 (Bar graph, Bar chart)는 범주가 있는 데이터 값을 직사각형의 막대로 표현하는 그래프입니다.
Matplotlib에서는 matplotlib.pyplot의 bar() 함수를 이용해서 막대 그래프를 간단하게 표현할 수 있습니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
x = np.arange(3)
years = ['2017', '2018', '2019']
values = [100, 400, 900]

plt.bar(x, values)
plt.xticks(x, years)
plt.show()
"""
width는 막대의 너비입니다. 디폴트 값은 0.8이며, 예제에서는 0.6으로 설정했습니다.
align은 틱 (tick)과 막대의 위치를 조절합니다. 디폴트 값은 ‘center’인데, ‘edge’로 설정하면 막대의 왼쪽 끝에 x_tick이 표시됩니다.
color는 막대의 색을 지정합니다.
edgecolor는 막대의 테두리 색을 지정합니다.
linewidth는 테두리의 두께를 지정합니다.
tick_label을 어레이 형태로 지정하면, 틱에 어레이의 문자열을 순서대로 나타낼 수 있습니다.
log=True로 설정하면, y축이 로그 스케일로 표시됩니다.
"""
plt.bar(x, values, width=0.6, align='edge', color="springgreen",
        edgecolor="gray", linewidth=3, tick_label=years, log=True)
plt.show()