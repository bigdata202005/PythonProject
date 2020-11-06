import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element, SubElement, dump
# 주석까지 읽기

# -------------------------------------------------------------------------
class CommentedTreeBuilder(ET.TreeBuilder):
    def __init__(self, *args, **kwargs):
        super(CommentedTreeBuilder, self).__init__(*args, **kwargs)

    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)


if __name__ == "__main__":
    print('---------------------------------------------------------')
    print('Before: ElementTree ogirinal parser() dump()')
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    dump(root)  # 주석은 읽지 않는다.
    # xml tree 를 파일로 저장한다.
    tree.write('original.xml', xml_declaration=True)  # 주석은 저장되지 않는다.
    print('---------------------------------------------------------')
    print('After:Commented parser dump')
    # 주석까지 읽으려면 파서를 지정해 줘야 한다.
    tree = ET.parse('sample.xml', parser=ET.XMLParser(target=CommentedTreeBuilder()))
    root = tree.getroot()
    dump(root) # 주석까지 읽었다

    # 읽은 내용을 다시 저장
    # xml tree 를 파일로 저장한다. 한글깨짐
    tree.write('commented_parser.xml')
    # 한글커멘트가 깨지 않도록 utf8 로 저장
    tree.write('commented_parser2.xml', encoding='utf8', xml_declaration=True)
