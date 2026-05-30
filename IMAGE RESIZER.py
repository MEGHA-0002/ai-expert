import cv2

# Load the image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Define three sizes (width, height)
sizes = [
    (800, 600),
    (400, 300),
    (200, 150)
]

# Resize, display, and save images
for i, size in enumerate(sizes, start=1):
    resized = cv2.resize(image, size)

    cv2.imshow(f"Resized Image {i}", resized)

    output_file = f"resized_{i}.jpg"
    cv2.imwrite(output_file, resized)

    print(f"Saved: {output_file}")

cv2.waitKey(0)
cv2.destroyAllWindows()