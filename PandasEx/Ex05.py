import pandas as pd
import numpy as np

# 누락된 데이터

"""
pandas는 주로 값 np.nan을 사용하여 누락 된 데이터를 나타냅니다. 
기본적으로 계산에 포함되지 않습니다. 
재 인덱싱을 사용하면 지정된 축에서 인덱스를 
변경 / 추가 / 삭제할 수 있습니다. 
이것은 데이터의 복사본을 반환합니다.
"""
dates = pd.date_range('20200901', periods=6)
# DataFrame : 2차원의 데이터
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print('~'*50)
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print(df1)
print('~'*50)
# 값 변경
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
print('~'*50)

# 누락 된 데이터가있는 행을 삭제합니다.
print(df1.dropna(how='any'))
print('~'*50)
# 누락 된 데이터가있는 행의 값을 채운다.
print(df1.fillna(value=5))
# 논리 배열 : NaN인곳만 True를 리턴
print(pd.isna(df1))

