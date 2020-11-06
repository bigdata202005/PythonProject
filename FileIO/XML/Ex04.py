# XML 만들기
from xml.etree.ElementTree import Element, dump
# 보기 좋게 xml만들기
root = Element("xml", kind="language")
node1 = Element("first", id="01")
node1.text = "안녕"
root.append(node1)

node2 = Element("second", id="02")
node2.text = "Hello"
root.append(node2)


def indent(elem, level=0): #자료 출처 https://goo.gl/J8VoDK
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


indent(root)
dump(root)

# 결과
"""
<xml kind="language">
  <first id="01">안녕</first>
  <second id="02">Hello</second>
</xml>
"""