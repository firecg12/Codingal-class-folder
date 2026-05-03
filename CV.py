try:
    import cv2
except ImportError:
    print("Error: opencv-python is not installed. Install it using: pip install opencv-python")
    exit()

# Load the image
image = cv2.imread("example.jpg")

# Check if image loaded correctly
if image is None:
    print("Image not found. Check the file name or path.")
else:
    # Print image dimensions
    print(f"Image Dimensions: {image.shape}")  # height, width, channels

    # Create a resizable window
    cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)

    # Resize the window only, not the actual image
    cv2.resizeWindow("Loaded Image", 800, 500)

    # Show the image
    cv2.imshow("Loaded Image", image)

    # Wait until any key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()