import pandas as pd
import numpy as np
"""
python을 통해 데이터 분석을 할때 기초 라이브러리로 사용되는 Numpy
-----------------------------------------------------------------
np.random.randint 균일 분포의 정수 난수 1개 생성
np.random.rand 0부터 1사이의 균일 분포에서 난수 matrix array생성
np.random.randn 가우시안 표준 정규 분포에서 난수 matrix array생성

np.random.shuffle 기존의 데이터의 순서 바꾸기
np.random.choice 기존의 데이터에서 sampling
np.unique 데이터에서 중복된 값을 제거하고 중복되지 않는 값의 리스트를 출력
np.bincount 발생하지 않은 사건에 대해서도 카운트를 해준다
"""
data_frame = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
print(data_frame)

data_frame.to_csv("./result.csv")
