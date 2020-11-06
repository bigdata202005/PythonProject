# XML 만들기
from xml.etree.ElementTree import ElementTree, Element, dump, SubElement, Comment
# indent를 모듈로 만들어서 사용
from FileIO.XML.indent import indent
# xml 저장
root = Element("xml", kind="language")
node1 = Element("first", id="01")
node1.text = "안녕"
root.append(node1)

node2 = Element("second")
node2.text = "Hello"
node2.attrib["id"] = "02"  # 또다른 속성추가
root.append(node2)

# 속성과 값을 한번에 추가하기
SubElement(root, "append", id="03").text= "반갑습니다"

# Comment () 함수는 xml 파일에 주석을 삽입하는 데 사용됩니다.
comment1 = Comment("XML comment")
root.append(comment1)

comment2 = Comment("XML 한글 comment")
root.append(comment2)

# 저장하기
ElementTree(root).write("test1.xml")  # 한글깨짐(encoding default 값이 'us-ascii')
# xml_declaration=True : XML문서 선언 포함
ElementTree(root).write("test2.xml", encoding='utf8',  xml_declaration=True)  # 한글 정상

# 들여쓰기 저장
indent(root)
ElementTree(root).write("test3.xml", encoding='utf8',  xml_declaration=True)  # 한글 정상

dump(root)
