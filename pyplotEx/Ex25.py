# Ex25.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 수평 막대 그래프 그리기
수평 막대 그래프는 범주가 있는 데이터 값을 수평 방향의 막대로 표현하는 그래프입니다.
matplotlib.pyplot의 barh() 함수를 이용하면 수평 막대 그래프를 그릴 수 있습니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
y = np.arange(3)
years = ['2017', '2018', '2019']
values = [100, 400, 900]

plt.barh(y, values, height=-0.6, align='edge', color="springgreen",
        edgecolor="gray", linewidth=3, tick_label=years, log=False)
plt.show()
"""
height는 막대의 높이입니다. 디폴트는 0.8인데 -0.6으로 설정했습니다.
align은 tick과 막대의 위치를 조절합니다. 디폴트는 ‘center’인데 ‘edge’로 설정하면 막대의 아래쪽 끝에 y_tick이 표시됩니다.
예제에서는 height를 음수로 지정했기 때문에 막대의 위쪽 끝에 y_tick이 표시됩니다.
color는 막대의 색을 지정합니다.
edgecolor는 막대의 테두리색을 지정합니다.
linewidth는 테두리의 두께를 지정합니다.
tick_label을 어레이 형태로 지정해주면, 틱에 어레이의 문자열을 순서대로 나타낼 수 있습니다.
log=False로 설정하면, x 축이 선형 스케일로 표시됩니다. 디폴트는 False입니다.
"""
