import numpy as np
import random as rd
import matplotlib.pyplot as plt

image = np.zeros((512,512))
for i in range(512):
    for j in range(512):
        image[i][j] = rd.randrange(0, 256, 1)
plt.imshow(image,cmap='gray')

plt.show()
