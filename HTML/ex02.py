from bs4 import BeautifulSoup

# 파일 읽기
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    print(soup.prettify())
print("~" * 50)

# 텍스트 읽기
soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
print(soup.prettify())

# 위의 두줄을 1줄로
print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", 'html.parser').prettify())