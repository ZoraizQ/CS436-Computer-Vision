from output import cartoonifier as c
import cv2
from matplotlib import pyplot as plt
import imageio
img = input("Drag an image: ")

plt.imshow(c(img))
plt.show()
