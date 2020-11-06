import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

image = cv2.imread("./image/cat.jpg", cv2.IMREAD_UNCHANGED)
fig, ax = plt.subplots()
im = ax.imshow(image)
patch = patches.Circle((260, 200), radius=100, transform=ax.transData)
im.set_clip_path(patch)
ax.axis('off')
plt.show()
