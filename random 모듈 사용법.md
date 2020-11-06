# random 모듈 사용법

파이썬의 random 모듈은 랜덤 숫자를 생성 뿐만 아니라 다양한 랜덤 관련 함수를 제공합니다.

## 모듈 임포트

우선 random 모듈을 사용하려면 임포트해야 합니다.

```py
import random
```

## random() 함수

0부터 1사이의 랜덤 실수를 리턴합니다.

```py
>>> random.random()        # Random float x, 0.0 <= x < 1.0
0.37444887175646646
```

## uniform() 함수

2개의 숫자 사이의 랜덤 실수를 리턴합니다.

```py
>>> random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
1.1800146073117523
```

## randint() 함수

2개의 숫자 사이의 랜덤 정수를 리턴합니다. (2번째 인자로 넘어온 정수도 범위에 포함시킴)

```py
>>> random.randint(1, 10)  # Integer from 1 to 10, endpoints included
7
```

## randrange() 함수

`range(start, stop, step)` 함수로 만들어지는 정수 중에 하나를 랜덤하게 리턴합니다.

```text
>>> random.randrange(0, 101, 2)  # Even integer from 0 to 100
26
```

## choice() 함수

랜덤하게 하나의 원소를 선택합니다.

```py
>>> random.choice('abcdefghij')  # Choose a random element
'c'
```

## sample() 함수

랜덤하게 여러 개의 원소를 선택합니다.

```py
>>> random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
[4, 1, 5]
```

## shuffle() 함수

원소의 순서를 랜덤하게 바꿉니다.

```python
>>> items = [1, 2, 3, 4, 5, 6, 7]
>>> random.shuffle(items)
>>> items
[7, 3, 2, 5, 6, 4, 1]
```

