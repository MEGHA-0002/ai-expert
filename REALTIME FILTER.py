import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

# Create window
cv2.namedWindow("Color Filter")

# Trackbar callback
def nothing(x):
    pass

# Create trackbars for RGB intensity
cv2.createTrackbar("Red", "Color Filter", 100, 200, nothing)
cv2.createTrackbar("Green", "Color Filter", 100, 200, nothing)
cv2.createTrackbar("Blue", "Color Filter", 100, 200, nothing)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Get trackbar values
    r = cv2.getTrackbarPos("Red", "Color Filter") / 100
    g = cv2.getTrackbarPos("Green", "Color Filter") / 100
    b = cv2.getTrackbarPos("Blue", "Color Filter") / 100

    # Split channels
    blue, green, red = cv2.split(frame)

    # Adjust intensities
    red = cv2.convertScaleAbs(red, alpha=r)
    green = cv2.convertScaleAbs(green, alpha=g)
    blue = cv2.convertScaleAbs(blue, alpha=b)

    # Merge channels
    filtered = cv2.merge([blue, green, red])

    cv2.imshow("Color Filter", filtered)

    key = cv2.waitKey(1)

    # Custom key presses
    if key == ord('r'):
        filtered = cv2.merge([np.zeros_like(blue), np.zeros_like(green), red])
        cv2.imshow("Color Filter", filtered)

    elif key == ord('g'):
        filtered = cv2.merge([np.zeros_like(blue), green, np.zeros_like(red)])
        cv2.imshow("Color Filter", filtered)

    elif key == ord('b'):
        filtered = cv2.merge([blue, np.zeros_like(green), np.zeros_like(red)])
        cv2.imshow("Color Filter", filtered)

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()