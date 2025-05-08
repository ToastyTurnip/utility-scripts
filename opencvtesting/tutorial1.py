import cv2

img = cv2.imread("./assets/illymap.png", cv2.IMREAD_COLOR)
print(img.shape)
img2 = cv2.resize(img, (500 , 500))
img3 = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img4 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("hello", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()