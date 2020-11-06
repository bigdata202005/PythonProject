import pandas as pd
import numpy as np

# 데이터 변경하기

dates = pd.date_range('20200901', periods=6)
# DataFrame : 2차원의 데이터
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print('~'*50)
# 열추가
df['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df)
print('~'*50)

s1 = pd.Series(list(range(1, 7)), index=pd.date_range('20200902', periods=6))
print(s1)
print('~'*50)
# 열추가 : index값을 찾아 자동으로 들어간다.
#          기존의 index가 없으면 사라진다. 없는 index는 NaN으로 저장된다.
#          1일은 NaN이되고 7일의 값은 사라졌다!!!
df['F'] = s1
print(df)
print('~'*50)
print(df.F)
print('~'*50)

# 값변경
df.at[dates[0], 'A'] = 0
print(df.at[dates[0], 'A'])

df.iat[1, 1] = 100
print(df.iat[1, 1])
print()
print(df)
print('~'*50)

# 범위를 지정하여 변경 가능
print(df.D)
print('~'*50)
df.loc[:, 'D'] = np.array([5] * len(df))
print(df.D)
print('~'*50)
print(np.array([5] * len(df)))
print('~'*50)

# 조건을 지정하여 값 변경
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df[df > 0] = -df  # 양수를 음수로 변경
print(df)
print('~'*50)


