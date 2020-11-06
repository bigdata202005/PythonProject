from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://datalab.naver.com/keyword/realtimeList.naver")
browser.get_screenshot_as_file('realtimeList1.png') # 스크린샷찍기
browser.quit()  # 브라우저 종료

browser = webdriver.Chrome()
browser.get("https://datalab.naver.com/keyword/realtimeList.naver")
browser.implicitly_wait(3)
browser.get_screenshot_as_file('realtimeList2.png') # 스크린샷찍기
browser.quit()  # 브라우저 종료


