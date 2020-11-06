import matplotlib.pyplot as plt
from PIL import Image

im = Image.open('./image/cat.jpg')
plt.imshow(im)
plt.axis('off')
plt.show()