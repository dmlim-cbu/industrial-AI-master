import cv2
import numpy as np

image = cv2.imread("lake.png", cv2.IMREAD_COLOR)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

case = input("D[dilation], E[erosion], O[open], C[close] 중 하나를 선택하세요. = ").upper()
loop = np.int(input("횟수 입력 하세요. = "))

mo_img = image.copy()

for i in range(loop):
    if case == "D":
        mo_img = cv2.dilate(mo_img, kernel)
    elif case == "E":
        mo_img = cv2.erode(mo_img, kernel)
    elif case == "O":
        kernel = np.ones((3, 3), np.uint8)
        erosion = cv2.erode(mo_img, kernel)
        mo_img = cv2.dilate(mo_img, kernel)
    elif case == "C":
        kernel = np.ones((3, 3), np.uint8)
        dilation = cv2.dilate(mo_img, kernel)
        mo_img = cv2.erode(mo_img, kernel)

cv2.imshow("result = " + case, mo_img)
cv2.waitKey()
cv2.destroyAllWindows()