# how to install opencv in python
try:
 import cv2
 import numpy as np
except ImportError:
    print("OpenCV or NumPy is not installed. Please install them using 'pip install opencv-python numpy'")


def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0  # Zero out green channel
        filtered_image[:, :, 0] = 0  # Zero out blue channel
    elif filter_type == "green_tint":
        filtered_image[:, :, 2] = 0  # Zero out red channel
        filtered_image[:, :, 0] = 0  # Zero out blue channel
    elif filter_type == "blue_tint":
        filtered_image[:, :, 2] = 0  # Zero out red channel
        filtered_image[:, :, 1] = 0  # Zero out green channel
    elif filter_type == "increased_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == "decreased_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)


    return filtered_image

image_path = "example.jpg"  # Update with your image path
image = cv2.imread(image_path)
if image is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    filter_type = "original"  # Change to desired filter type
    
    print("Press the following keys to apply filters:")
    print("r: Red Tint")
    print("g: Green Tint")
    print("b: Blue Tint")
    print("i: Increased Red")
    print("d: Decreased Blue")
    print("o: Original Image")
    print("q: Quit")
    
    while True:
        filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('i'):
            filter_type = "increased_red"
        elif key == ord('d'):
            filter_type = "decreased_blue"
        elif key == ord('o'):
            filter_type = "original"
        elif key == ord('q'):
            break
        else:
            print("Invalid key. Please try again.")
cv2.destroyAllWindows()