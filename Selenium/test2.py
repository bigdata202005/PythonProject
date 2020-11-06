import os
import time
import cv2
# pip install opencv-python
# 다운받을 이미지 url
url = "https://dispatch.cdnser.be/cms-content/uploads/2020/04/09/a26f4b7b-9769-49dd-aed3-b7067fbc5a8c.jpg"

# time check
# start = time.time()

# curl 요청
os.system("curl " + url + " > test.png")

# 이미지 다운로드 시간 체크
# print(time.time() - start)

# 저장 된 이미지 확인
a = cv2.imread('test.jpg')
cv2.imshow('test', a)
cv2.waitKey()



