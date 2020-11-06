"""
Q18 문자열 검색
다음 코드의 결괏값은 무엇일까?

import re
p = re.compile("[a-z]+")
m = p.search("5 python")
m.start() + m.end()
"""
import re
p = re.compile("[a-z]+")
m = p.search("5 python")
print(m.start(), m.end())
print(m.start() + m.end()) # 2 + 8 = 10
"""
2 8
10   
"""