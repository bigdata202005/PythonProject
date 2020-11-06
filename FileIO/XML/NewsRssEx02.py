from urllib.request import Request, urlopen
from xml.etree import ElementTree

URL = "http://rss.hankyung.com/new/news_main.xml"
req = Request(URL, method="GET")
res = urlopen(req)
data = res.read().decode('utf-8')
print(type(data))
print(data)
print("*" * 80)

root = ElementTree.fromstring(data)
print(type(root))
ElementTree.dump(root)
print("*" * 80)

# 태그읽기
print("루트태그 :", root.tag)
print("루트속성 :", root.attrib)
print("*" * 80)

channel = root.find("channel")
print(channel.find("title").text)
print(channel.find("link").text)
print(channel.find("description").text)
print("*" * 80)

items = channel.findall("item")
print(type(items))
for item in items:
    print(item.find('title').text)
    print(item.find('link').text)
    print(item.find('description').text)
    print("-" * 80)
