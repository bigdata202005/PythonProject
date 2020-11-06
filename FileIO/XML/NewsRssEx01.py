from urllib.request import Request, urlopen
import xmltodict

URL = "http://rss.hankyung.com/new/news_main.xml"
req = Request(URL, method="GET")
res = urlopen(req)
data = res.read().decode('utf-8')
print(type(data))
print(data)
print("*" * 80)

xml_dict = xmltodict.parse(data)
print(xml_dict)
print("*" * 80)

print(xml_dict["rss"]["channel"]["title"])
print(xml_dict["rss"]["channel"]["link"])
print(xml_dict["rss"]["channel"]["pubDate"])
print("*" * 80)
for item in xml_dict["rss"]["channel"]["item"]:
    print(item["title"])
    print(item["link"])
    print(item["description"])
    print("-" * 80)

