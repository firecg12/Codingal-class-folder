try:
    import cv2
    import matplotlib.pyplot as plt
except ImportError:
    print("Please install the required libraries: opencv-python and matplotlib")
    exit()

image = cv2.imread('example.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title('RGB Image')
plt.show()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap='gray')
plt.title('Grayscale Image')
plt.show()

cropped_image = image[100:300, 200:400]
plt.imshow(cropped_image)
plt.title('Cropped Image')
plt.show()
