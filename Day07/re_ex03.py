# 파이선 정규표현식에 사용되는 모듈
import re

# 참조
# https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/07/20/regex-usage-01-basic/

"""
[자주 사용하는 문자 클래스]

[0-9] 또는 [a-zA-Z] 등은 무척 자주 사용하는 정규 표현식이다. 
이렇게 자주 사용하는 정규식은 별도의 표기법으로 표현할 수 있다. 다음을 기억해 두자.

\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.
대문자로 사용된 것은 소문자의 반대임을 추측할 수 있다.
"""
"""
정규식을 이용한 문자열 검색
이제 컴파일된 패턴 객체를 사용하여 문자열 검색을 수행해 보자. 컴파일된 패턴 객체는 다음과 같은 4가지 메서드를 제공한다.

Method	    목적
match()	    문자열의 처음부터 정규식과 매치되는지 조사한다.
search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
match, search는 정규식과 매치될 때는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려준다. 
"""
p = re.compile('[a-z]+')
m = p.match("python")  # <re.Match object; span=(0, 6), match='python'>
print(m)

m = p.match("3 python")  # None
print(m)

print('~' * 80)

m = p.match('python')
if m:
    print('Match found: ', m.group())
else:
    print('No match')

m = p.match('3 python')
if m:
    print('Match found: ', m.group())
else:
    print('No match')

print('~' * 80)
m = p.search('python')
if m:
    print('search found: ', m.group())
else:
    print('No search')

m = p.search('3 python')
if m:
    print('search found: ', m.group())
else:
    print('No search')
print('~' * 80)

#  [a-z]+ 정규식과 매치해서 리스트로 돌려준다.
result = p.findall("life is too short 123 !@# qwerty Python")
print(result)  # ['life', 'is', 'too', 'short', 'qwerty', 'ython']