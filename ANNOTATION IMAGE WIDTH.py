import cv2

# Load image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Calculate arrow positions
y = height // 2
start_point = (20, y)
end_point = (width - 20, y)

# Draw bi-directional arrow
cv2.arrowedLine(image, start_point, end_point, (0, 255, 0), 2, tipLength=0.03)
cv2.arrowedLine(image, end_point, start_point, (0, 255, 0), 2, tipLength=0.03)

# Add width label
text = f"Width = {width} pixels"
text_position = (width // 4, y - 20)

cv2.putText(
    image,
    text,
    text_position,
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 0, 0),
    2
)

# Display image
cv2.imshow("Width Annotation", image)

# Save annotated image
cv2.imwrite("annotated_width.jpg", image)

print("Annotated image saved as 'annotated_width.jpg'")

cv2.waitKey(0)
cv2.destroyAllWindows()