import xml.etree.ElementTree as ET
# XML 파일읽기
tree = ET.parse('data2.xml')
root = tree.getroot()
ET.dump(root)
print("*" * 80)

# 태그읽기
print("루트태그 :", root.tag)
print("루트속성 :", root.attrib)
print("루트내용 :", root.text)
print("*" * 80)

# for loop을 통해 iteration 하는 예시
for child in root:
    print(child.tag, child.attrib)
print("*" * 80)

# iter method를 활용한 iteration 예시
for rank in root.iter('rank'):
     print("{} : {}".format(rank.tag, rank.text))
print("*" * 80)

# index를 이용한 예시
print("{} : {}".format(root[0][1].tag, root[0][1].text))
print("{} : {}".format(root[1][1].tag, root[1][1].text))
print("{} : {}".format(root[2][1].tag, root[2][1].text))
# print("{} : {}".format(root[3][1].tag, root[3][1].text))  # 에러
print("*" * 80)

#  findall method 활용
for country in root.findall('country'):
    rank = country.find("rank").text  # 내용읽기
    name = country.get("name")
    print("{} : {}".format(rank, name))
