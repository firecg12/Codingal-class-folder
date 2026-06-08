import cv2
import numpy as np

# Display size
width, height = 1000, 700

def apply_filter(image, filter_type):
    """Apply the selected color filter or edge detection."""

    filtered_image = image.copy()

    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Green channel
        filtered_image[:, :, 0] = 0  # Blue channel

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0  # Blue channel
        filtered_image[:, :, 2] = 0  # Red channel

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0  # Green channel
        filtered_image[:, :, 2] = 0  # Red channel

    elif filter_type == "sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

        sobelx = cv2.convertScaleAbs(sobelx)
        sobely = cv2.convertScaleAbs(sobely)

        combined_sobel = cv2.bitwise_or(sobelx, sobely)

        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)

    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray_image, 100, 200)

        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image


# Load image
image_path = "example.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")

else:
    filter_type = "original"

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("s - Sobel Edge Detection")
    print("c - Canny Edge Detection")
    print("q - Quit")

    # Create a resizable window
    cv2.namedWindow("Filtered Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Filtered Image", width, height)

while True:

    # Check if window was closed
    if cv2.getWindowProperty("Filtered Image", cv2.WND_PROP_VISIBLE) < 1:
        print("Window closed.")
        break

    filtered_image = apply_filter(image, filter_type)

    display_image = cv2.resize(
        filtered_image,
        (width, height),
        interpolation=cv2.INTER_CUBIC
    )

    cv2.imshow("Filtered Image", display_image)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('r'):
            filter_type = "red_tint"

    elif key == ord('g'):
            filter_type = "green_tint"

    elif key == ord('b'):
            filter_type = "blue_tint"

    elif key == ord('s'):
            filter_type = "sobel"

    elif key == ord('c'):
            filter_type = "canny"

    elif key == ord('q'):
            # Exit animation
            for i in range(5):
                dots = "." * (i + 1)
                print(f"Exiting{dots}", end="\r")
                cv2.waitKey(300)

            print("\nGoodbye!")
            break


    else:
            print("Invalid key! Please use r, g, b, s, c, or q.")

cv2.destroyAllWindows()