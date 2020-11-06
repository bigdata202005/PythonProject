from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://datalab.naver.com/keyword/realtimeList.naver")

browser.implicitly_wait(1)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
ranking_box = soup.find("div",{'class':'ranking_box'})
# print(ranking_box)
for rank in ranking_box.find_all("li",{'class':'ranking_item'}):
    # print(rank)
    rank_str = rank.find_all('span')[0].text
    title = rank.select('span span.item_title')[0].text
    print(rank_str, title )
browser.quit()  # 브라우저 종료