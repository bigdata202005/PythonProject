import requests

webpage = requests.get("https://www.daangn.com/hot_articles")
webpage.encoding = 'utf-8'
print(webpage.url)
print("_" * 80)
print(webpage.status_code)
print("_" * 80)
print(webpage.cookies)
print("_" * 80)
print(str(webpage.content))
print("_" * 80)
print(str(webpage.content.decode('utf-8')))
print("_" * 80)
print(webpage.encoding)
print("_" * 80)
print(webpage.headers)
print("_" * 80)
print(webpage.history)
print("_" * 80)
# print(webpage.text)
# print("_" * 80)