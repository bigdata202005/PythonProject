from urllib.request import Request, urlopen
from xml.etree import ElementTree

URL = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4113566500"
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

for child in root.find('channel'):
    print(child.tag)

print("*" * 80)
print(root.find('channel').find('title').tag) # 'title'
print(root.find('channel').find('title').attrib) # 'title'
print(root.find('channel').find('title').text) # 'title'
print(root.find('channel').find('item').find('title').text) # 'title'
print(root.find('channel').find('item').find('link').text) # 'title'
print(root.find('channel').find('item').find('description').find('body').find('data').get('seq')) # 'title'
print(root.find('channel').find('item').find('description').find('body').find('data').find('temp').text) # 'title'
print("*" * 80)

items = root.find('channel').find('item').find('description').find('body').findall('data');
print(type(items))
for item in items:
    print(item.get("seq") + ". " + item.find("temp").text)
