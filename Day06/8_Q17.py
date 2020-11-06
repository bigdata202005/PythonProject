"""
Q17 기초 메타 문자
다음 중 정규식 a[.]{3,}b과 매치되는 문자열은 무엇일까?

acccb
a....b
aaab
a.cccb
"""
import re

p = re.compile("a[.]{3,}b")
print(p.match("acccb"))
print(p.match("acccb") and "일치" or "불일치")
print(p.match("a....b"))
print(p.match("a....b") and "일치" or "불일치")
print(p.match("aaab"))
print(p.match("aaab") and "일치" or "불일치")
print(p.match("a.cccb"))
print(p.match("a.cccb") and "일치" or "불일치")