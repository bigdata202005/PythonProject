from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True  # 창이 나타나지 않는다.
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("http://sports.khan.co.kr/comics/comic_newest.html")
browser.implicitly_wait(1)
soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)
# print(soup.select("div#container div div h5"))
# print(soup.select("div#container div div ul"))
comics_list = []
uls = soup.select("div#container div div ul")
# print(len(uls), "개")
for ul in uls:
    lis = ul.select("li")
    # print(len(lis), "개")
    # print("~" * 80)
    for li in lis:
        # print(li.select('img')[0].attrs['alt'], end=' :')
        name = li.select('img')[0].attrs['alt']
        # print(li.select('img')[0].attrs['src'])
        img = li.select('img')[0].attrs['src']
        # print(li.select('a')[0].attrs['href'])
        link = li.select('a')[0].attrs['href']
        comics_list.append({"name": name, "img": img, 'link': link})  # 만화 목록 저장

print('~' * 80)
print("만화 개수 : ", len(comics_list), "개!!!", sep='')
print('~' * 80)


def get_comics(link):
    browser.get(link)
    browser.implicitly_wait(3)
    html = BeautifulSoup(browser.page_source, 'html.parser')
    total_page = len(html.select("div.page_num a"))
    print("전체 페이지 :", total_page)
    page_link = "http://freecomics.sportskhan.net/"
    id = link.split("=")[1]
    page_link = page_link + id + "/"
    return_str = ""
    for page in range(1, total_page + 1):
        for i in range(1, 100):
            img_src = page_link + "{:03d}/{:03d}.jpg".format(page, i)
            return_str += "<img onerror=\"this.style.display='none'\" src='" + img_src + "'>\n"
    return return_str

for comic in comics_list:
     file = open("./comic/" + comic['name'].strip('\n') +".html", "w")
     html = get_comics(comic['link'])
     file.write(html)
     file.close()

