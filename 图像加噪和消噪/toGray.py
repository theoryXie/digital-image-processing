import cv2

img = cv2.imread("gray.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# cv2.imwrite("gray.jpg", img_gray)
