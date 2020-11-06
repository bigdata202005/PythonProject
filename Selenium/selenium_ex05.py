from selenium import webdriver
# 네이버에 로그인하기
options = webdriver.ChromeOptions()
# options.add_argument('headless')  # 창을 띄우지 않고!!!!
options.add_argument('window-size=1920x1080') # 창의 크기
# 2개 중에 1개
# options.add_argument("disable-gpu")
# options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', options=options)
driver.get('http://naver.com')
driver.implicitly_wait(1)
elem = driver.find_element_by_class_name("link_login")
elem.click()
driver.implicitly_wait(1)
# 예전에는 이렇게 됐었다!!!
# id = driver.find_element_by_id("id")
# id.send_keys('네이버아이디')
# driver.implicitly_wait(1)
# pw = driver.find_element_by_id("pw")
# pw.send_keys('네이버비번')
# driver.implicitly_wait(1)

# --------------------------------------------------------------------------
id= "네이버 아이디";
pw= "네이버 비밀번호";

driver.execute_script("document.getElementById('id').value='"+ id + "'")
driver.execute_script("document.getElementById('pw').value='"+ pw + "'")
driver.find_element_by_id("log.login").click()
# --------------------------------------------------------------------------

# driver.quit()





