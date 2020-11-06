# XML 만들기
from xml.etree.ElementTree import Element, dump
# 속성 추가하기
root = Element("xml", kind="language")
node1 = Element("first", id="01")
node1.text = "안녕"
root.append(node1)

node2 = Element("second", id="02")
node2.text = "Hello"
root.append(node2)
dump(root)

# 결과
"""
<xml kind="language"><first id="01">안녕</first><second id="02">Hello</second></xml>
"""