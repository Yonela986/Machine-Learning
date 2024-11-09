import cv2
import numpy as np

def cartoonify_image(image):
    """
    Apply the cartoon effect to the given image.
    Steps: 
    1. Apply bilateral filter for smoothing while preserving edges.
    2. Convert the image to grayscale.
    3. Detect edges using adaptive thresholding.
    4. Combine edges and smoothed image to create cartoon effect.
    """

    # Step 1: Apply Bilateral Filter is used to smooth the image while preserving the edges, which is a key characteristic of cartoon images.
    bilateral_filter = cv2.bilateralFilter(image, d=9, sigmaColor=300, sigmaSpace=300)

    # Step 2: Convert to Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 3: Detect Edges using Adaptive Thresholding
    edges = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Step 4: Combine edges and filtered image
    cartoon_image = cv2.bitwise_and(bilateral_filter, bilateral_filter, mask=edges)

    return cartoon_image
