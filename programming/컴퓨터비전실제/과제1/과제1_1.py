import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("lake.png", cv2.IMREAD_COLOR)
img_eq = image.copy()
b, g, r = cv2.split(image)
inverse = cv2.merge((r, g, b))

keyin = input("R, B, G 중 하나를 입력하세요. Color : ")

if keyin == "R":
    eq = cv2.equalizeHist(r)
    img_eq = cv2.merge((b, b, eq))
elif keyin == "G":
    eq = cv2.equalizeHist(g)
    img_eq = cv2.merge((b, eq, b))
elif keyin == "B":
    eq = cv2.equalizeHist(b)
    img_eq = cv2.merge((eq, g, g))

hist, bins = np.histogram(eq, 256, [0, 255])
plt.fill(hist)
plt.xlabel('histogram')
plt.show()

cv2.imshow("orginal image", image)
cv2.imshow("equalize color = " + keyin, img_eq)
cv2.waitKey()
cv2.destroyAllWindows()