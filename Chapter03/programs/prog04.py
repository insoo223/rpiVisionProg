import matplotlib.pyplot as plt
import numpy as np

#x = np.array([[0, 1, 2, 3, 4],
#              [5, 6, 7, 8, 9]], dtype = np.uint8 )

x = np.random.rand(3,3,3)
plt.imshow(x)
#plt.imshow(x, cmap='Accent') # Green to colorful to Blk
#plt.imshow(x, cmap='spring')
#plt.imshow(x) # Blk to yellow
#plt.imshow(x, cmap='gray') # Blk to gray
plt.axis('off')
plt.grid('off')

plt.show()

#print(plt.colormaps())
