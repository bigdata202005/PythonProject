from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)
print('~' * 80)
print(soup.prettify())
print('~' * 80)
print(soup.title)  # <title>태그 읽기
print(soup.title.name) # 태그명
print(soup.title.string) # 태그내용
print(soup.title.parent.name)  # 부모태그 이름
print()

p = soup.p  # 첫번째 p태그
print(type(p))  # <class 'bs4.element.Tag'>
print(p)  # <p class="title"><b>The Dormouse's story</b></p>
print(p.name)
print(p.string)
print(soup.p['class'])  # 속성읽기
print()

a = soup.find_all('a')
print(type(a))
print(a)
print("=" * 80)
for tag in a:
    print(tag['class'])
    print(tag['href'])
    print(tag['id'])
    print(tag.string)
    print("~" * 80)


print(soup.find(id="link3"))
print()

print(soup.get_text())  # 모든 텍스트만