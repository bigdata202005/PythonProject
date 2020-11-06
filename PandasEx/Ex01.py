import pandas as pd
import numpy as np
# 1차원 데이터
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print("~" * 80)

dates = pd.date_range('20200901', periods=6)
print(dates)
print("~" * 80)
# dates = pd.date_range('20200901', periods=10)
# print(dates)
# print("~" * 80)


# DataFrame : 2차원의 데이터
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print("~" * 80)

# dict형식으로 생성
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print("~" * 80)

print(df2.dtypes)
print("~" * 80)
print(df2.A)
print("~" * 80)

# 데이터보기
# 프레임의 상단 및 하단 행을 보는 방법은 다음과 같습니다.
print(df2.head())
print("~" * 80)
print(df2.head(2)) # 상위 2개만
print("~" * 80)

print(df2.tail())
print("~" * 80)
print(df2.tail(3)) # 하위 3개만
print("~" * 80)

# 색인, 열을 표시합니다.
print("index :",df2.index)        # 인덱스
print("columns :",df2.columns)      # 컬럼보기
print("~" * 80)

# numpy데이터로 변환
# DataFrame.to_numpy()출력에 색인 또는 열 레이블이 포함 되지 않습니다 .
ar = df.to_numpy()
print(type(ar))
print(ar)
print("~" * 80)

ar2 = df2.to_numpy()
print(type(ar2))
print(ar2)
print("~" * 80)

# describe() 데이터에 대한 빠른 통계 요약을 보여줍니다.
print(df.describe())
print("~" * 80)
print(df2.describe())
print("~" * 80)

# 행열 치환 : T
df3 = df.T
print(df)
print("~" * 80)
print(df3)
print("~" * 80)

# 정렬
# 1. 축으로 정렬
sort_df = df.sort_index(axis=1, ascending=False) # 열 내림차순 정렬
print(sort_df)
print("~" * 80)

sort_df = df.sort_index(axis=0, ascending=False) # 행 내림차순 정렬
print(sort_df)
print("~" * 80)

sort_df = df.sort_index(axis=0)  # 행 오름차순 정렬
print(sort_df)
print("~" * 80)

# 2. 값으로 정렬
sort_value_df = df.sort_values(by='B') # B열 오름차순
print(sort_value_df)
print("~" * 80)

sort_value_df = df.sort_values(by='B', ascending=False) # B열 내림차순
print(sort_value_df)
print("~" * 80)


