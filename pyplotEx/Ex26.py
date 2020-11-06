# Ex26.py
import matplotlib.pyplot as plt
import numpy as np
"""
Matplotlib 산점도 그리기
산점도 (scatter plot)는 두 변수의 상관 관계를 직교 좌표계의 평면에 데이터를 
점으로 표현하는 그래프입니다.
matplotlib.pyplot 모듈의 scatter() 함수를 이용하면 산점도를 그릴 수 있습니다.
"""
# 한글깨짐. 반드시 폰트 적용해야 함
plt.rc('font', family='NanumGothicCoding')
plt.xlabel('X축값')
plt.ylabel('Y축값 ')
plt.suptitle('그래프 제목')
plt.gcf().canvas.set_window_title('윈도우제목')
"""
np.random.seed()를 이용해서 난수 생성의 시드를 설정하면, 같은 난수를 재사용할 수 있습니다.
seed()에 들어갈 파라미터는 0에서 4294967295 사이의 정수여야 합니다.
"""
np.random.seed(19680801)
N = 50
"""
x, y의 위치, 마커의 색 (colors)과 면적 (area)을 무작위로 지정해줍니다.
예를 들어, x는 [0.7003673, 0.74275081, … ,0.23722644, 0.82394557]으로 0~1 범위에서 
무작위의 50 개의 값을 갖습니다.
"""
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
print(x)
print('~' * 50)
print(y)
print('~' * 50)
print(area)
print('~' * 50)
print(colors)
print('~' * 50)
"""
scatter()에 x, y 위치를 입력해줍니다.
s는 마커의 면적을, c는 마커의 색을 지정합니다.
alpha는 마커 색의 투명도를 결정합니다.
"""
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()