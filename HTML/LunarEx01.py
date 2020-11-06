import requests
url = "https://astro.kasi.re.kr/life/pageView/5"
webpage = requests.get(url)
print(str(webpage.content.decode('utf-8')))
print("_" * 80)
