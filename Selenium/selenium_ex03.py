from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 창을 띄우지 않고!!!!
options.add_argument('window-size=1920x1080') # 창의 크기
# 2개 중에 1개
# options.add_argument("disable-gpu")
# options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', options=options)
driver.get('http://naver.com')
driver.implicitly_wait(1)
driver.get_screenshot_as_file('naver_main_headless.png')
driver.quit()
print("저장완료!!!!")




