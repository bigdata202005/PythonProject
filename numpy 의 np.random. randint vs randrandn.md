## numpy 의 np.random. `randint` vs `rand/randn`

np.random.seed seed를 통한 난수 생성

np.random.**randint** 균일 분포의 정수 난수 1개 생성
np.random.**rand** 0부터 1사이의 균일 분포에서 난수 matrix array생성
np.random.**randn** 가우시안 표준 정규 분포에서 난수 matrix array생성

np.random.shuffle 기존의 데이터의 순서 바꾸기
np.random.choice 기존의 데이터에서 sampling
np.unique 데이터에서 중복된 값을 제거하고 중복되지 않는 값의 리스트를 출력
np.bincount 발생하지 않은 사건에 대해서도 카운트를 해준다

In [1]:

```
import numpy as np
```

### random.`randint` 와 np.random.randint : 모두 (시작, n-1) 사이의 `랜덤숫자 1개` 뽑아내기

In [3]:

```
np.random.randint(6) # 0 or 1 or ~ or 5      0부터 5까지 랜덤한 숫자 1개 
```

Out[3]:

```
5
```

In [4]:

```
np.random.randint(1, 20) # 1부터 19까지 랜덤숫자 1개
```

Out[4]:

```
19
```

### np.random.`rand(m,n)` : 0 ~ 1의 균일분포 `표준정규분포` 난수를 `matrix array`(m,n) 생성

In [5]:

```
np.random.rand(6)  
```

Out[5]:

```
array([0.82374834, 0.03504426, 0.19848749, 0.47607174, 0.98983665,
       0.63021609])
```

In [6]:

```
np.random.rand(3,2)
```

Out[6]:

```
array([[0.21023055, 0.46075628],
       [0.99993567, 0.29630209],
       [0.79509783, 0.05405658]])
```

### np.random.`randn(m,n)` : 평균0, 표준편차1의 가우시안 `표준정규분포` 난수를 `matrix array`(m,n) 생성

In [7]:

```
np.random.randn(6)
```

Out[7]:

```
array([ 0.42240858,  0.39214236, -0.05216362, -0.31037385, -1.75930161,
        0.04749234])
```

In [8]:

```
np.random.randn(3, 2)
```

Out[8]:

```
array([[ 1.65238965, -0.75137173],
       [-1.59079976, -1.26309433],
       [ 0.20991563,  2.23786713]])
```