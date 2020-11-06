import re
"""
DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
"""
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.S)
m = p.match('a\nb')
print(m)

print("~" * 80)
p = re.compile('[a-z]')
rs1 = p.match('python')
rs2 = p.match('Python')
rs3 = p.match('PYTHON')
print(rs1)
print(rs2)
print(rs3)

p = re.compile('[a-z]', re.IGNORECASE)
rs1 = p.match('python')
rs2 = p.match('Python')
rs3 = p.match('PYTHON')
print(rs1)
print(rs2)
print(rs3)

p = re.compile('[a-z]', re.I)
rs1 = p.match('python')
rs2 = p.match('Python')
rs3 = p.match('PYTHON')
print(rs1)
print(rs2)
print(rs3)

print("~" * 80)
data = """python one
life is too short
python two
you need python
python three"""
p = re.compile("^python\s\w+") #  ^(시작)\s(whitespace)\w(단어) +(1개이상)
print(p.findall(data))  # ['python one']
print("-" * 80)

p = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data))
print("-" * 80)

p = re.compile("^python\s\w+", re.M)
print(p.findall(data))
print("-" * 80)

print("~" * 80)
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|[0-9a-fA-F]+);')     #0[0-7] or 0-9]+ or [0-9a-fA-F]+

charref = re.compile(r"""
&[#]                                    # Start of a numeric entity reference
(
    0[0-7]+                             # Octal form
    |[0-9]+                             # Decimal form
    |[0-9a-fA-F]+                       # Hexadcimal form
)                                       # Trailing semicolon
;""", re.VERBOSE)

p = re.compile(r'\\section')
print(p)
p = re.compile('\\\\section')
print(p)
