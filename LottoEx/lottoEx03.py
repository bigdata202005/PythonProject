from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def read_table():
    tr_elements = driver.find_elements_by_css_selector("table.tbl_data tbody tr")
    lotto_list = list()
    for e in tr_elements:
        e1 = e.find_elements_by_css_selector("td")
        key = e1[0].text
        value = e1[1].text.split(',')
        value = list(map(lambda x: int(x), value))
        lotto_dict = {key: value}
        lotto_list.append(lotto_dict)
    print(lotto_list)
    return lotto_list


options = webdriver.ChromeOptions()
# options.add_argument('headless')  # 창을 띄우지 않고!!!!
options.add_argument('window-size=1920x1080')  # 창의 크기
driver = webdriver.Chrome('chromedriver', options=options)
driver.get('https://dhlottery.co.kr/common.do?method=main')
driver.implicitly_wait(5)
driver.find_element_by_partial_link_text("당첨결과").click()
driver.implicitly_wait(3)
driver.find_element_by_partial_link_text("당첨내역").click()
driver.implicitly_wait(3)
# select박스 찾아
select = Select(driver.find_element_by_id('drwNoStart'))
# 값을 1로 변경하고
# select by visible text
# select.select_by_visible_text('1')
# select by value
select.select_by_value('1')
driver.implicitly_wait(3)
# 조회버튼 클릭
driver.find_element_by_partial_link_text("조회").send_keys(Keys.RETURN)
driver.implicitly_wait(3)
# 마지막페이지 클릭
driver.find_element_by_partial_link_text("끝 페이지").send_keys(Keys.RETURN)
driver.implicitly_wait(3)

my_lotto_list = list()
while True:
    # 페이지 번호를 찾아
    elements = driver.find_elements_by_css_selector("#page_box a")
    elements.reverse()
    e = None
    for e in elements:
        my_lotto_list.append(read_table())
        if '페이지' not in e.text:
            print("태그명 :", e.tag_name, e.text, "페이지 읽기", e.get_attribute('href'), e.get_attribute('onclick'))
            # e.send_keys(Keys.RETURN)
            # driver.implicitly_wait(5)
            # my_lotto_list.append(read_table())
    if e.text == '1':
        break
    driver.find_element_by_partial_link_text("이전 페이지").send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

# driver.quit()  # 브라우저 종료
