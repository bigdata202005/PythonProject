import pandas as pd
import numpy as np

dates = pd.date_range('20200901', periods=6)
# DataFrame : 2차원의 데이터
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print('~'*50)
print(df.mean())  # 행방향 평균(NaN제외)
print('~'*50)
print(df.mean(1))  # 열방향 평균(NaN제외)
print('~'*50)
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
print('~'*50)
print(df1.mean())  # 행방향 평균(NaN제외)
print('~'*50)
print(df1.mean(1))  # 열방향 평균(NaN제외)
print('~'*50)
