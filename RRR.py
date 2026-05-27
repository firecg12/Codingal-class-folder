import cv2

import numpy as np




def display_image(title, image):

    """Utility function to display an image."""

    cv2.imshow(title, image)

    cv2.waitKey(0)  # Wait forever until any key is pressed

    cv2.destroyAllWindows()



def apply_color_filter(image, filter_type, intensity=50):

    """Apply the specified color filter to the image."""

    filtered_image = image.copy()

    error_handling(filter_type, intensity)

    if filter_type == "red_tint":

        filtered_image[:, :, 1] = 0  # Green channel to 0

        filtered_image[:, :, 0] = 0  # Blue channel to 0



    elif filter_type == "blue_tint":

        filtered_image[:, :, 1] = 0  # Green channel to 0

        filtered_image[:, :, 2] = 0  # Red channel to 0



    elif filter_type == "green_tint":

        filtered_image[:, :, 0] = 0  # Blue channel to 0

        filtered_image[:, :, 2] = 0  # Red channel to 0



    elif filter_type == "increase_red":

        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], intensity)



    elif filter_type == "decrease_blue":

        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], intensity)



    elif filter_type == "increase_green":

        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], intensity)



    elif filter_type == "decrease_red":

        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], intensity)



    return filtered_image

def error_handling(filter_type, intensity):
    """Handle errors for invalid filter types and intensity values."""

    valid_filters = ["red_tint", "blue_tint", "green_tint", "increase_red", "decrease_blue", "increase_green", "decrease_red"]

    if filter_type not in valid_filters:

        raise ValueError(f"Invalid filter type: {filter_type}. Valid options are: {', '.join(valid_filters)}")



    if not (0 <= intensity <= 255):

        raise ValueError("Intensity must be between 0 and 255.")


def save_image(image):

    """Allow the user to save the filtered image."""

    filename = input("Enter a name for the image: ")

    filename = "".join(c for c in filename if c.isalnum() or c in ('_', '-'))  # Sanitize filename

    cv2.imwrite(f"images/{filename}.png", image)

    print(f"Image saved as {filename}.png")


def change_orientation(image):
    """Change the orientation of the image."""
    # the user presses 'right arrow' key, rotate the image 90 degrees clockwise
    while True:
        key = cv2.waitKey(0)

        if key == 27:  # ESC key to exit
            break

        elif key == 81:  # Left arrow key
            image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        elif key == 83:  # Right arrow key
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

        display_image("Rotated Image", image)

def interactive_color_filter(image_path):

    """Interactive activity for real-time color filter application."""

    image = cv2.imread(image_path)

    if image is None:

        print("Error: Image not found!")

        return



    print("Select an option:")

    print("r = Red Tint")

    print("b = Blue Tint")

    print("g = Green Tint")

    print("i = Increase Red Intensity")

    print("d = Decrease Blue Intensity")

    print("u = Increase Green Intensity")

    print("d = Decrease Red Intensity")

    print("q = Quit")

    print("NOTE: You can also change the orientation of the image by pressing the left or right arrow keys.")



    while True:

        filter_type = input("Enter your choice: ")



        if filter_type == "r":

            filtered_image = apply_color_filter(image, "red_tint")

        elif filter_type == "b":

            filtered_image = apply_color_filter(image, "blue_tint")

        elif filter_type == "g":

            filtered_image = apply_color_filter(image, "green_tint")

        elif filter_type == "i":

            filtered_image = apply_color_filter(image, "increase_red", intensity=50)

        elif filter_type == "d":

            filtered_image = apply_color_filter(image, "decrease_blue", intensity=50)

        elif filter_type == "u":

            filtered_image = apply_color_filter(image, "increase_green", intensity=50)

        elif filter_type == "d":
            filtered_image = apply_color_filter(image, "decrease_red", intensity=50)

        elif filter_type == "q":

            print("Exiting...")

            break

        else:

            print("Invalid choice. Please select a valid option.")



        display_image("Filtered Image", filtered_image)

        save_choice = input("Do you want to save the image? (yes/no): ")

        if save_choice.lower() == "yes":

            save_image(filtered_image)




interactive_color_filter('example.jpg')