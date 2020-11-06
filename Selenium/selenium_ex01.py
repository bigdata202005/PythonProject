from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://python.org")
browser.get_screenshot_as_file('python_main.png') # 스크린샷찍기
browser.quit()  # 브라우저 종료

browser = webdriver.Chrome()
browser.get("https://naver.com")
browser.get_screenshot_as_file('naver_main.png') # 스크린샷찍기
browser.quit()  # 브라우저 종료