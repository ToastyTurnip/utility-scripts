import cv2, random
import numpy as np

img = cv2.imread("./assets/illymap.png", cv2.IMREAD_COLOR)

# accessing pixels
for i in range(10):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0,255)]

# accessing squares
img2 = np.array(img[200:400, 400:600])
img[0:200, 200:400] = img2

print(img)
print(img2.shape)

cv2.imshow("hello", img)
cv2.waitKey(0)
cv2.destroyAllWindows()