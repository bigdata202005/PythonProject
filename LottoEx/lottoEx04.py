import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

"""
엑셀 파일을 읽어서 json파일로 만들어 놓는다.
"""
lotto = None
with open("lotto.json", 'r', encoding="utf-8-sig") as json_file:
    lotto = json.load(json_file)
total_count = 0
if lotto is not None:
    total_count = len(lotto)
print("전체개수 :", total_count)
# ------------------------------------------------------
options = webdriver.ChromeOptions()
options.add_argument('headless')  # 창을 띄우지 않고!!!!
options.add_argument('window-size=1920x1080')  # 창의 크기
driver = webdriver.Chrome('chromedriver', options=options)
driver.get('https://dhlottery.co.kr/gameResult.do?method=allWin')
# select박스 찾아
select = Select(driver.find_element_by_id('drwNoStart'))
# 가장 최근의 10개주 데이터를 읽기위해 회수를 변경
select.select_by_value(str(total_count-9))
driver.implicitly_wait(3)
# 조회버튼 클릭
driver.find_element_by_partial_link_text("조회").send_keys(Keys.RETURN)
driver.implicitly_wait(3)
# 데이터를 읽어 파일내용을 읽은 dict에 추가한다. key는 횟수이다.
# 이미 같은 회수가 있으면 겹쳐쓴다.
tr_elements = driver.find_elements_by_css_selector("table.tbl_data tbody tr")
for e in tr_elements:
    e1 = e.find_elements_by_css_selector("td")
    key = e1[0].text
    value = e1[1].text.split(',')
    value = list(map(lambda x: int(x), value))
    lotto[key] = value

total_count = len(lotto)
print("전체개수 :", total_count)
driver.quit()  # 브라우저 종료

# 다시 저장한다.
# json 파일로 저장
with open('lotto.json', 'w', encoding='utf-8') as make_file:
    json.dump(lotto, make_file, indent="\t")