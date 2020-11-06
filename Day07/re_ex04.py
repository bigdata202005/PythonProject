# 파이선 정규표현식에 사용되는 모듈
import re

"""
match 객체의 메서드를 사용하면 이 같은 궁금증을 해결할 수 있다. 다음 표를 보자.

method	목적
group()	매치된 문자열을 돌려준다.
start()	매치된 문자열의 시작 위치를 돌려준다.
end()	매치된 문자열의 끝 위치를 돌려준다.
span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
"""

p = re.compile("[a-z]+")
m = p.match("python")
print("match 결과 객체 :", type(m))
print(m.group())
print(m.start())
print(m.end())
print(m.span())
"""
결과
match 객체 : <class 're.Match'>
python
0
6
(0, 6)
"""
# m = p.search("123 python qwerty")
m = re.search('[a-z]+', "123 python qwerty")
print("search 결과 객체 :", type(m))
print(m.group())
print(m.start())
print(m.end())
print(m.span())
"""
search 결과 객체 : <class 're.Match'>
python
4
10
(4, 10)
"""