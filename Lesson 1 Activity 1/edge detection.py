import cv2
import numpy as np
import matplotlib.pyplot as plt

# Utility function to display an image
def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# Main function for interactive edge detection and filtering
def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    while True:
        print("\nSelect an option:")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Smoothing")
        print("5. Median Filtering")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Sobel Edge Detection
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == "2":
            # Canny Edge Detection
            threshold1 = int(input("Enter lower threshold (default: 100): ") or 100)
            threshold2 = int(input("Enter upper threshold (default: 200): ") or 200)
            edges = cv2.Canny(gray_image, threshold1, threshold2)
            display_image("Canny Edge Detection", edges)

        elif choice == "3":
            # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            laplacian_abs = cv2.convertScaleAbs(laplacian)
            display_image("Laplacian Edge Detection", laplacian_abs)

        elif choice == "4":
            # Gaussian Smoothing
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): ") or 5)
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Smoothed Image", blurred)

        elif choice == "5":
            # Median Filtering
            print("Adjust kernel size for Median filtering (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): ") or 5)
            median_filtered = cv2.medianBlur(image, kernel_size)
            display_image("Median Filtered Image", median_filtered)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Provide the path to an image for the activity
interactive_edge_detection('example.jpg')
