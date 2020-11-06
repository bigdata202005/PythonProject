# XML 만들기
from xml.etree.ElementTree import Element, dump
# 노드에 노드 추가하기
root = Element("xml")
node1 = Element("first")
node1.text = "안녕"
root.append(node1)

node2 = Element("second")
node2.text = "Hello"
root.append(node2)

dump(root)

# 결과
"""
<xml><first>안녕</first><second>Hello</second></xml>
"""