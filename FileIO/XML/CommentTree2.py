import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump

# 모듈로 만들어서 사용
from FileIO.XML.CommentTree import CommentedTreeBuilder

print('---------------------------------------------------------')
print('Before: ElementTree ogirinal parser() dump()')
tree = ET.parse('sample.xml')
root = tree.getroot()
dump(root)
# xml tree 를 파일로 저장한다.
tree.write('original.xml', xml_declaration=True)
print('---------------------------------------------------------')
print('After:Commented parser dump')
tree = ET.parse('sample.xml', parser=ET.XMLParser(target=CommentedTreeBuilder()))
root = tree.getroot()
dump(root)
# xml tree 를 파일로 저장한다. 한글깨짐
tree.write('commented_parser.xml')
# 한글커멘트가 깨지 않도록 utf8 로 저장
tree.write('commented_parser2.xml', encoding='utf8', xml_declaration=True)
