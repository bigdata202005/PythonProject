import cv2
import numpy as np

image = cv2.imread("./image/cat.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("cat", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
