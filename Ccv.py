import cv2
# Load the image
image = cv2.imread("example.jpg")

#convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#resize the image to 224x224
resized_image = cv2.resize(gray_image, (224, 224))

#display the resized image
cv2.imshow("Resized Image", resized_image)
#wait until a key is pressed and close the window
k = cv2.waitKey(0)

if k == ord('s'):
    cv2.imwrite("resized_image.jpg", resized_image)
    print("Image saved as resized_image.jpg")
cv2.destroyAllWindows()

print(f"Processed Image Dimensions: {resized_image.shape}")  # height, width
