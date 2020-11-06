# XML 만들기
from xml.etree.ElementTree import Element, dump

# Element() 함수로 노드를 만들고 text로 값을 지정합니다.
node1 = Element("first")
node1.text = "안녕"
dump(node1)

# 결과
"""
<first>안녕</first>
"""

