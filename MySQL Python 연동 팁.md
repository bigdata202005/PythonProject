# MySQL Python 연동 팁

### Tip. execute()/executemany()에 Placeholder 사용하기

만약 DB내 데이터에 대해 대량 삽입/변경/삭제가 필요한데, 조건이 다 다르다면?
**Placeholder**를 이용할 수 있습니다!

Placeholder란, 위와 같이 동적 SQL문을 구성할 때 유용하게 사용할 수 있는 기능인데요.
동적 값이 들어갈 위치에 `%s`를 이용해 SQL문을 만들어 놓고,
execute() 계열 메서드 첫번째 파라미터에는 SQL을, 두번째 파라미터에 실제 데이터를 리스트나 튜플 형태로 넣어주면 됩니다.

```
excute(SQL, a-data)`
`executemany(SQL, multiple-data)
```

하나의 데이터만 적용시킬 거라면 execute()를,
여러 개의 데이터를 한 번에 대량으로 적용시킬 거라면 executemany()를 사용하면 됩니다.

Placeholder의 특징은,

- 두번째 파라미터에 들어간 데이터 순서대로 SQL이 적용되고,
- 특히 문자의 경우 따옴표 등의 특수문자들이 자동으로 이스케이프(Escape)되어 처리됩니다. (완전 간편!)
- 문자열, 숫자 등에 관계 없이 대치할 값은 모두 `%s`로 쓰입니다. (일반 문자열에서 사용하는 `%s`, `%d`와는 다름)
- `%s`는 컬럼 값을 대치할 때만 사용할 수 있습니다.

예시를 들어보겠습니다.

#### 1) `execute()`

```
data = ('ramen', 1)

# SELECT 
sql = "SELECT * FROM `food` WHERE name = %s AND id = %s;"
cursor.execute(sql, data)

# DELETE
sql = "DELETE FROM `food` WHERE `name` = %s AND `id` = %s;"
cursor.execute(sql, data)
db.commit()
```

문자열 값이여도 %s를 따옴표로 감싸지 않아도 됩니다.
`%s` 위치대로 `data`가 구성되어야 제대로 동작하니 유의하세요!

#### 2) `executemany()`

```
data = [['ramen', 1], ['fried rice', 2], ['chicken', 3]]

# INSERT 
sql = "INSERT INTO `food`(name, id) VALUES (%s, %s);"
cursor.executemany(sql, data)
db.commit()

# UPDATE 
sql = "UPDATE `food` SET `name` = %s WHERE `id` = %s;"
cursor.executemany(sql, data)
db.commit()
```

이차원 배열 혹은 이차원 튜플을 사용하여 데이터를 구성합니다.
데이터 순서대로 DB에 적용됩니다.
반복문 + execute() 메서드를 사용하는 것보다 **훨-씬** 속도와 메모리 면에서 효율적입니다.
(몇 십 만에서 몇 백 만 데이터 UPDATE시 반복문 + execute()는 몇 시간, executemany()는 몇 분 컷!)

------

이렇게 간단하게 MySQL과 Python을 연동하여 DB의 데이터를 조작하는 방법에 대해 알아봤습니다.
이 기본 사용법을 좀 더 응용하면 분석 결과나 전처리 결과를 바로 DB에 반영하는 것도 쉽겠지요?
더 많은 함수는 [PyMySQL Documentation (바로가기)](https://pymysql.readthedocs.io/en/latest/index.html)를 참조하세요!
한국어 설명은 [예제로 배우는 파이썬 프로그래밍 - Python DB API](http://pythonstudy.xyz/python/article/201-Python-DB-API) 이 사이트를 참조하세요!