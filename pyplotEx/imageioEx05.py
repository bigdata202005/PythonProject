import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

im = Image.open('./image/cat.jpg')
plt.imshow(im)
ax = plt.gca()
rect = patches.Rectangle((90, 20),
                         150,
                         200,
                         linewidth=1,
                         edgecolor='cyan',
                         fill=False)
ax.add_patch(rect)
rect = patches.Rectangle((220, 20),
                         230,
                         230,
                         linewidth=3,
                         edgecolor='red',
                         fill=False)
ax.add_patch(rect)
circle = patches.Circle((200,200),radius=60, linewidth=1, edgecolor='blue', fill=False)
ax.add_patch(circle)

plt.show()

