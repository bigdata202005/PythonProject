import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20200901', periods=6)
# DataFrame : 2차원의 데이터
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# dict형식으로 생성
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

# 얻기
print(df)
print("~" * 80)
# 열 얻기
print(df['A'])          # A열
print("~" * 80)
print(df.A)             # A열
print("~" * 80)
print(df[['A', 'C']])   # A, C열
print("~" * 80)
# 행 얻기
print(df[0:2])          # 0~2행
print("~" * 80)
print(df[3:])           # 3행이후 모두
print("~" * 80)
print(df['20200902':'20200904'])    # index 값으로 범위지정
print("~" * 80)

# 라벨로 선택
print(df.loc[dates[0]])  # 1행
print("~" * 80)
print(df.loc[dates[3]])  # 1행
print("~" * 80)
print(df.loc[:, ['A', 'B']])  # 모든행의 A,B열
print("~" * 80)
print(df.loc['20200902':'20200904', ['A', 'B']])  # 2~4일까지 A,B열
print("~" * 80)
print(df.loc['20200902', ['A', 'B']]) # 2일 A,B열
print("~" * 80)
print(df.loc['20200902', 'A'])  # 2일 A열
print("~" * 80)
print(df.loc[dates[1], 'A'])  # 2일 A열
print("~" * 80)
print(df.at['20200902', 'A'])  # 2일 A열 : at사용
print("=" * 80)

# 위치 별 선택
print(df.iloc[0])   # 9월 1일 데이터
print(df.iloc[3])   # 9월 4일 데이터
print("~" * 80)
print(df.iloc[3:5, 0:2])    # 4~5일행  A,B열
print("~" * 80)
print(df.iloc[[1, 2, 4], [0, 2]])   # 배열로 인덱스값 전송
print("~" * 80)                     # 2,3,5행 A, C열

print(df.iloc[1:3, :]) # 행을 명시적으로 : 2~3행
print("~" * 80)
print(df.iloc[:, 1:3]) # 열을 명시적으로 : BC열
print("~" * 80)
print(df.iloc[1, 1])
print(df.iat[1, 1])
print("~" * 80)




