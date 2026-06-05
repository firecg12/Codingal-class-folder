import cv2

# Load image
img = cv2.imread("example.jpg")

# Resize first (2x larger)
img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Rotate back to upright
height, width = img.shape[:2]
center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(center, -15, 1.0)
rotated = cv2.warpAffine(
    img,
    rotation_matrix,
    (width, height),
    flags=cv2.INTER_CUBIC
)

# Increase brightness and clarity
bright = cv2.convertScaleAbs(rotated, alpha=1.3, beta=30)

# Crop around the butterfly
cropped = bright[150:700, 150:700]

# Show larger windows
cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.namedWindow("Brightened", cv2.WINDOW_NORMAL)
cv2.namedWindow("Cropped", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Rotated", 500, 300)
cv2.resizeWindow("Brightened", 500, 300)
cv2.resizeWindow("Cropped", 500, 300)

cv2.imshow("Rotated", rotated)
cv2.imshow("Brightened", bright)
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()