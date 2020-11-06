import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True # 창이 나타나지 않는다.
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://movie.naver.com/")
browser.implicitly_wait(1)
browser.find_element_by_id("_all_view_go").click()
thumb = browser.find_elements_by_css_selector("ul.lst_detail_t1 li")
movie_img_list = list()
movie_name_list = list()
for li in thumb:
    movie_img_list.append(li.find_element_by_tag_name('img').get_attribute('src'))
    movie_name_list.append(li.find_element_by_css_selector('dl dt.tit a').text)

print("영화제목 :", movie_name_list)
print("영화이미지 :", movie_img_list)

for i in range(0,len(movie_img_list)):
    print(movie_name_list[i], " :", movie_img_list[i])
    os.system("curl " + movie_img_list[i] + " > ./images/" + movie_name_list[i].replace(' ','_') + ".jpg")

print("저장완료!!!!")
