import numpy as np
import cv2

keyin = input("boat1(1), budapest1(2), newpaper1(3), s1(4) 4개의 영상중 하니를 선택해 주세요. : ")

if keyin == "1":
    image = cv2.imread('stitching/boat1.jpg', cv2.IMREAD_COLOR)
    image = cv2.resize(image, None, fx=0.2, fy=0.2)
elif keyin == "2":
    image = cv2.imread('stitching/budapest1.jpg', cv2.IMREAD_COLOR)
    image = cv2.resize(image, None, fx=0.5, fy=0.5)
elif keyin == "3":
    image = cv2.imread('stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
    image = cv2.resize(image, None, fx=0.5, fy=0.5)
elif keyin == "4":
    image = cv2.imread('stitching/s1.jpg', cv2.IMREAD_COLOR)
    image = cv2.resize(image, None, fx=0.5, fy=0.5)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
edges = cv2.Canny(hsv, 100, 200)

cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge', edges)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

corners = cv2.cornerHarris(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
corners = cv2.dilate(corners, None)

show_img = np.copy(image)
show_img[corners>0.1*corners.max()]=[0,0,255]

corners = cv2.normalize(corners, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
show_img = np.hstack((show_img, cv2.cvtColor(corners, cv2.COLOR_GRAY2BGR)))

cv2.imshow('Harris corner detector', show_img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
