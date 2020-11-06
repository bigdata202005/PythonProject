from selenium import webdriver
import time
# https://www.instagram.com/에 로그인하기
options = webdriver.ChromeOptions()
# options.add_argument('headless')  # 창을 띄우지 않고!!!!
options.add_argument('window-size=1920x1080') # 창의 크기


driver = webdriver.Chrome('chromedriver', options=options)
driver.get('https://www.instagram.com/')
driver.implicitly_wait(3)

driver.find_element_by_name("username").send_keys('bigdata202005@gmail.com')
driver.find_element_by_name("password").send_keys('woaldjqtek2')
time.sleep(2)
driver.find_element_by_id("loginForm").click()
# --------------------------------------------------------------------------

# driver.quit()





