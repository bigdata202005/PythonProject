# sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.
import re
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))
# colour socks and colour shoes : blue, red 두개 변경
print(p.sub('colour', 'blue socks and red shoes', count=1))
# colour socks and red shoes : blue만 변경

print(p.subn('colour', 'blue socks and red shoes'))
# ('colour socks and colour shoes', 2) : 결과를 튜프로 알려준다.

p = re.compile('abc1234')
password = p.sub('def5678', 'abc1234')      # 기존 비밀번호 변경 시 적용
print(password)

# 이름 전화  ==> 전화 이름
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))

print("~" * 80)

# 찾은 문자열을 16진수 숫자 문자로 변경해분다.
def hexrepl(match):
    value = int(match.group())  # 넘어온 문자를 숫자로 변환
    return hex(value) # 16진수로 변환하여 리턴

# 숫자만
p = re.compile(r'\d+')
# sub(함수, 내용)
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
# Call 0xffd2 for printing, 0xc000 for user code.

# 전화번호 + 정규식 예
p = re.compile(r"\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m)

p = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*$')
m = p.match("ankiwoong@cj.net")
print(m)

m = p.match("ankiwoongcj.net")
print(m)