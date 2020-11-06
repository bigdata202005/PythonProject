from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('headless')  # 창을 띄우지 않고!!!!
options.add_argument('window-size=1920x1080') # 창의 크기
# 2개 중에 1개
# options.add_argument("disable-gpu")
# options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', options=options)
driver.get('http://naver.com')
driver.implicitly_wait(1)
elem = driver.find_element_by_name("query")
# 입력 부분에 default로 값이 있을 수 있어 비운다
elem.clear()
# 검색어를 입력한다
elem.send_keys("Selenium")
#검색을 실행한다
elem.submit()


# driver.quit()





