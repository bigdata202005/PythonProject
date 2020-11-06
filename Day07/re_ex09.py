import re
# 그룹핑 - 이름 중간자리 별표
p = re.compile(r"(\w)(\w)(\w)")
m = p.search("한사람")
print(m)
print(m.group(1) + "*" + m.group(3))

# 그룹핑 - 전화번호 중간자리 별표
p = re.compile(r"(\d+)[-](\d+)[-](\d+)")
m = p.search("010-2345-6789")
print(m)
print(m.group(1) + "-****-" + m.group(3))

# 오타 중복 추출
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
print(p.search('한 사 사 람').group())
