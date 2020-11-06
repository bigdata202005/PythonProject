# Ex28.py
import matplotlib.pyplot as plt
import numpy as np

"""
Matplotlib 히스토그램 그리기
히스토그램 (Histogram)은 도수분포표를 그래프로 나타낸 것으로서, 
가로축은 계급, 세로축은 도수 (횟수나 개수 등)를 나타냅니다.
계급은 보통 변수의 구간이며 서로 겹치지 않습니다.
matplotlib.pyplot 모듈의 hist() 함수를 이용해서 간단한 히스토그램을 그려 보겠습니다.

weight는 몸무게 값을 나타내는 리스트입니다.
hist() 함수에 리스트의 형태로 값들을 직접 입력해주면 됩니다.
"""
weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71, 80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
plt.hist(weight)
plt.show()
"""
여러 개의 히스토그램 그리기
Numpy의 np.random.randn(), np.random.standard_normal(), np.random.rand() 함수를 이용해서 
임의의 값들을 만들었습니다.
어레이 a는 표준편차 2.0, 평균 1.0을 갖는 정규분포, 
어레이 b는 표준정규분포를 따릅니다.
어레이 c는 -10.0에서 10.0 사이의 균일한 분포를 갖는 5000개의 임의의 값입니다.
세 개의 분포를 동시에 그래프에 나타냅니다.
bins는 몇 개의 영역으로 쪼갤지를 설정합니다.
density=True로 설정해주면, 밀도함수가 되어서 막대의 아래 면적이 1이 됩니다.
alpha는 투명도를 의미합니다. 0.0에서 1.0 사이의 값을 갖습니다.
histtype을 ‘step’으로 설정하면 막대 내부가 비어있고, ‘stepfilled’로 설정하면 막대 내부가 채워집니다.
"""
a = 2.0 * np.random.randn(10000) + 1.0
b = np.random.standard_normal(10000)
c = 20.0 * np.random.rand(5000) - 10.0

plt.hist(a, bins=100, density=True, alpha=0.7, histtype='step')
plt.hist(b, bins=50, density=True, alpha=0.5, histtype='stepfilled')
plt.hist(c, bins=100, density=True, alpha=0.9, histtype='step')
plt.show()