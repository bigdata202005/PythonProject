import imageio
import matplotlib.pyplot as plt

im = imageio.imread('http://upload.wikimedia.org/wikipedia/commons/d/de/Wikipedia_Logo_1.0.png')
plt.axis('off')
plt.imshow(im)  # 이미지를 그래프에 설정
plt.imsave('./image/logo.png', im)
plt.show()  # 보이기

im = imageio.imread('imageio:chelsea.png')
print(im.shape)
plt.imshow(im)  # 이미지를 그래프에 설정
plt.axis('off')
plt.show()