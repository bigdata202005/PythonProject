# () : 그룹
import re
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m)
print(m.group(2))

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
name = m.group(1)
tel = m.group(2)
# 전체
print(m.group())
print(m.group(0))
# 1개씩
print(name)
print(tel)

"""
group(인덱스)	설명
group(0)	    매치된 전체 문자열
group(1)	    첫 번째 그룹에 해당되는 문자열
group(2)	    두 번째 그룹에 해당되는 문자열
group(n)	    n 번째 그룹에 해당되는 문자열
"""

p = re.compile(r"(\d+)\s+(\w+)\s+(\w+)")
m = p.search("20190217 Sunny 20도")
date = m.group(1)
weather = m.group(2)
degree = m.group(3)
print("오늘의 날짜는 {} 입니다.".format(date))
print("오늘의 날씨는 {} 입니다.".format(weather))
print("금일 온도는 {} 입니다.".format(degree))

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-](\d+))")
m = p.search("park 010-1234-4567")
first_num = m.group(3)
last_num = m.group(4)
print(first_num)
print(last_num)

# 재참조 : \1
p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())

# 그룹에 이름지정
p = re.compile(r'(?P<name>\w+)\s+(?P<tel>(\d+)[-]\d+[-]\d+)')
m = p.search('park 010-1234-1234')
print(m.group('name'))
print(m.group('tel'))

# 재참조
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('Paris in the the spring').group())
print(p.search('Paris in the the spring').group(1))
print("~" * 80)

# 전방탐색
p = re.compile('.+:')
m = p.search('http://google.com')
print(m.group())

"""
전방 탐색에는 긍정(Positive)과 부정(Negative)의 2종류가 있고 다음과 같이 표현한다.

긍정형 전방 탐색((?=...)) - ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
부정형 전방 탐색((?!...)) - ...에 해당되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
"""
p = re.compile('.+(?=:)')
m = p.search('http://google.com')
print(m.group())

p = re.compile('.+(?=//)')
m = p.search('http://google.com')
print(m.group())

p = re.compile('.*[.].*$')
m = p.search('sendmail.cf')
print(m.group())
m = p.search('foo.bar')
print(m.group())
m = p.search('autoexec.bat')
print(m.group())

p = re.compile('.*[.][^b].*$') # [^b] : 확장자가 b로 시작되는것은 제외
m = p.search('sendmail.cf')
print(m)
m = p.search('foo.bar')
print(m)
m = p.search('autoexec.bat')
print(m)
print("~" * 80)

p = re.compile('.*[.][b].*$') # [b] : 확장자가 b로 시작되는것
m = p.search('sendmail.cf')
print(m)
m = p.search('foo.bar')
print(m)
m = p.search('autoexec.bat')
print(m)
print("~" * 80)

p = re.compile('.*[.]([^b]..|.[^a].|..[^t])$')
# b로 시작하면 안되고, 중간 글자가 a면 안되고, 끝 문자가 t면 안됨
m = p.search('sendmail.cf') # 두글자라 제외
print(m)
m = p.search('foo.bar')
print(m)
m = p.search('autoexec.bat')
print(m)
print("~" * 80)

p = re.compile('.*[.](?!bat$).*$')
m = p.search('sendmail.cf') # 두글자라 제외
print(m)
m = p.search('foo.bar')
print(m)
m = p.search('autoexec.bat')
print(m)
print("~" * 80)

p = re.compile('.*[.](?!bat$|bar$).*$')
m = p.search('sendmail.cf') # 두글자라 제외
print(m)
m = p.search('foo.bar')
print(m)
m = p.search('autoexec.bat')
print(m)
print("~" * 80)



