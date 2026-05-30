import cv2

# Load the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# 1. Rotate the image by 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# 2. Brighten the image
brightened = cv2.convertScaleAbs(rotated, alpha=1.0, beta=50)

# 3. Crop the image (adjust coordinates as needed)
height, width = brightened.shape[:2]
cropped = brightened[50:height-50, 50:width-50]

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)
cv2.imshow("Brightened Image", brightened)
cv2.imshow("Cropped Image", cropped)

# Save transformed images
cv2.imwrite("rotated_image.jpg", rotated)
cv2.imwrite("brightened_image.jpg", brightened)
cv2.imwrite("cropped_image.jpg", cropped)

print("Images saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()