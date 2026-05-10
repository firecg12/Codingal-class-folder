try:
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError as e:
    print(f"Error importing libraries: {e}")
    exit(1)

img = cv2.imread('example.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

(H, W) = img.shape[:2]
center = (W // 2, H // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img_rgb, M, (W, H))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title('Rotated Image')
plt.show()

brightness_matrix = np.ones(rotated_rgb.shape, dtype="uint8") * 50
brightened = cv2.add(rotated_rgb, brightness_matrix)

brightened_rgb = cv2.cvtColor(brightened, cv2.COLOR_BGR2RGB)
plt.imshow(brightened_rgb)
plt.title('Brightened Image')
plt.show()
