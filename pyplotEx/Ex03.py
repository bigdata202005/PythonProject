# Ex03.py

import matplotlib.pyplot as plt
"""
스타일 지정하기
x, y 값 인자에 대해 선의 색상과 형태를 지정하는 포맷 문자열을 세번째 인자에 입력할 수 있습니다.
기본 포맷 문자열은 ‘b-‘인데 파란색 (‘blue’)의 선 (‘-‘)을 의미합니다.
아래의 ‘ro’는 빨간색 (‘red’)의 원형 (‘o’) 마커를 의미합니다.
또한, axis()를 이용해서 축의 범위 [xmin, xmax, ymin, ymax]를 지정해주었습니다.
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()