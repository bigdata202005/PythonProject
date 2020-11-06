import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20200901', periods=6)
# DataFrame : 2차원의 데이터
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

# 부울 인덱싱
# 단일열을 사용하여 지정
print(df['A'] > 0)
print("~"*50)
print(df[df['A'] > 0])
print("~"*50)

# 부울 조건이 충족되는 DataFrame에서 값 선택.
print(df>0)
print("~"*50)
print(df[df>0])
print("~"*50)

# isin()필터링 사용 방법
df2 = df.copy(deep=True)
print(df2)
print("~"*50)
# 열 추가
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2.E)
print("~"*50)
# E열의 값이 'two', 'four'인 값만
print(df2[df2['E'].isin(['two', 'four'])])



