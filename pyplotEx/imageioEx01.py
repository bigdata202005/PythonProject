import imageio
import matplotlib.pyplot as plt

image = imageio.imread('./image/image.jpg')  # 이미지 읽기
plt.imshow(image)  # 이미지를 그래프에 설정
plt.show()  # 보이기
plt.imsave('./image/image_new.jpg', image)  # 이미지 저장

image_new = imageio.imread('./image/image_new.jpg')
plt.imshow(image_new)
plt.show()
