import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False  # 화면 숨기기/보이기를 이렇게도 지정 가능하다.
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

time.sleep(1)
select = browser.find_element_by_css_selector("span.select_btn")
# print(select)
select.click()
# select2 = browser.find_elements_by_css_selector("div.select ul li")
# # for li in select2:
# #     print(li.text)
# select2[7].click()
browser.find_element_by_partial_link_text("스포츠/레저").click()

# 조회버튼 클릭
browser.find_element_by_css_selector("a.btn_submit").click()
time.sleep(1)
# 1페이지 읽고
# 내용읽기
tag_names = browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
for tag in tag_names:
    print(tag.text.split("\n"))

# 다음 페이지 링크 클릭
browser.find_element_by_css_selector("a.btn_page_next").click()
# 일시 멈춤
time.sleep(1)
# 2페이지 내용읽기
tag_names = browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
for tag in tag_names:
    print(tag.text.split("\n"))
