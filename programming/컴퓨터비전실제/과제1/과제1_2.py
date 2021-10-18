import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("lake.png").astype(np.float32) / 255

noised = (image + 0.5 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0, 1)

Diameter = np.int(input("Diameter : "))
sc = np.double(input("Sigma Color : "))
ss = np.double(input("Sigma Space : "))

#OpenCV has a function called bilateralFilter() with the following arguments:
#d: Diameter of each pixel neighborhood.
#sigmaColor: Value of \sigma in the color space. The greater the value, the colors farther to each other will start to get mixed.
#sigmaColor: Value of \sigma in the coordinate space. The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.
bilateral = cv2.bilateralFilter(image, Diameter, sc, ss)

cv2.imshow("original", image)
cv2.imshow("noised", noised)
cv2.imshow("bilateral Filter", bilateral)
cv2.waitKey()
cv2.destroyAllWindows()