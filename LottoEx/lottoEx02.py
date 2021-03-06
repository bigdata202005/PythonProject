from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def read_table():
    elements = driver.find_elements_by_css_selector("table.tbl_data tbody tr")
    lotto_list = list()
    for e in elements:
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
driver.implicitly_wait(1)
driver.find_element_by_partial_link_text("당첨결과").click()
driver.implicitly_wait(1)
driver.find_element_by_partial_link_text("당첨내역").click()
driver.implicitly_wait(1)

select = Select(driver.find_element_by_id('drwNoStart'))
# select by visible text
# select.select_by_visible_text('1')
# select by value
select.select_by_value('1')
driver.implicitly_wait(2)
driver.find_element_by_partial_link_text("조회").send_keys(Keys.RETURN)
driver.implicitly_wait(2)
driver.find_element_by_partial_link_text("끝 페이지").send_keys(Keys.RETURN)
driver.implicitly_wait(3)

elements = driver.find_elements_by_css_selector("#page_box a")
total_page = int(elements[len(elements) - 1].text)
print("전체 페이지 :", total_page)

while True:
    print(total_page, "읽기")
    read_table()
    total_page -= 1
    if total_page % 10 == 0:
        if total_page == 0:
            break
        else:
            driver.find_element_by_partial_link_text("이전 페이지").send_keys(Keys.RETURN)
            driver.implicitly_wait(2)
            continue
    driver.find_element_by_partial_link_text(str(total_page)).send_keys(Keys.RETURN)
    driver.implicitly_wait(2)

# driver.quit()  # 브라우저 종료
