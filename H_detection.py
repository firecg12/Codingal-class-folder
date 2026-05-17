import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
      """Utility function to display an image."""
      plt.figure(figsize=(8, 8))
      if len(image.shape) == 2:
            plt.imshow(image, cmap='gray')
      else:
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
      plt.title(title)
      plt.axis('off')
      plt.show()

def interactive_edge_detection(image_path):
        """Interactive activity for edge detection and filtering."""
      # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Unable to load image at {image_path}")
            return
    
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        display_image("Original Grayscale Image", gray)
        
        print("Select an option: ")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Smoothing")
        print("5. Median Filtering")
        print("6. Exit")
        
        while True:
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                # Sobel Edge Detection
                sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
                sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
                combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
                display_image("Combined Sobel Edges", combined_sobel)
            elif choice == '2':
                 
                print("Adjusting thresholds for Canny (default: 100, 200)")
                lower = int(input("Enter lower threshold: "))
                upper = int(input("Enter upper threshold: "))
                edges = cv2.Canny(gray, lower, upper)
                display_image("Canny Edges", edges)
            elif choice == '3':
                # Laplacian Edge Detection
                laplacian = cv2.Laplacian(gray, cv2.CV_64F)
                display_image("Laplacian Edges", np.abs(laplacian).astype(np.uint8))
            
            elif choice == '4':  
                # Gaussian Smoothing
                print("Adjusting kernel size for Gaussian Smoothing (default: 5)")
                ksize = int(input("Enter kernel size (odd number): "))
                blurred = cv2.GaussianBlur(gray, (ksize, ksize), 0)
                display_image("Gaussian Blurred Image", blurred)
            elif choice == '5':
                # Median Filtering
                print("Adjusting kernel size for Median Filtering (default: 5)")
                ksize = int(input("Enter kernel size (odd number): "))
                median_filtered = cv2.medianBlur(image, ksize)
                display_image("Median Filtered Image", median_filtered)
            elif choice == '6':
                print("Exiting interactive edge detection............")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
if __name__ == "__main__":
    image_path = 'example.jpg'  # Update with your image path
    interactive_edge_detection(image_path)