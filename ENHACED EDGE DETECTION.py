import cv2

# Load image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

while True:
    print("\n===== MENU =====")
    print("1. Gaussian Filter")
    print("2. Median Filter")
    print("3. Sobel Edge Detection")
    print("4. Canny Edge Detection")
    print("5. Laplacian Edge Detection")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = cv2.GaussianBlur(gray, (5, 5), 0)
        cv2.imshow("Gaussian Filter", result)

    elif choice == "2":
        result = cv2.medianBlur(gray, 5)
        cv2.imshow("Median Filter", result)

    elif choice == "3":
        result = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)
        cv2.imshow("Sobel Edge Detection", result)

    elif choice == "4":
        result = cv2.Canny(gray, 100, 200)
        cv2.imshow("Canny Edge Detection", result)

    elif choice == "5":
        result = cv2.Laplacian(gray, cv2.CV_64F)
        cv2.imshow("Laplacian Edge Detection", result)

    elif choice == "6":
        break

    else:
        print("Invalid choice!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("Program Ended.")