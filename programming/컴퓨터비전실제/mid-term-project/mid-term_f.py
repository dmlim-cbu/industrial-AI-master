import numpy as np
import cv2
import matplotlib.pyplot as plt

keyin = input("r, g, y 신호등 이미지를 선택해 주세요. : ")

if keyin == "r": image = cv2.imread("sigb_r.jpg")
elif keyin == "g": image = cv2.imread("sigb_g.jpg")
elif keyin == "y": image = cv2.imread("sigb_y.jpg")

print("image : ", image.shape)

print("ROI를 마우스로 선택 하시고, ' x ' 를 입력해 주세요!!")

show_img = np.copy(image)
mouse_pressed = False

x, y, h, w = 400, 100, 500, 1200

def mouse_callback(event, _x, _y, flags, param):
    global show_img, x, y, w, h, mouse_pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        x, y = _x, _y
        show_img = np.copy(image)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            show_img = np.copy(image)
            cv2.rectangle(show_img, (x, y), (_x, _y), (0, 255, 0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        w, h = _x, _y

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', show_img)
    k = cv2.waitKey(1)

    if k == ord('x') and not mouse_pressed:
        if w * h > 0:
            break

cv2.destroyAllWindows()

dst_roi = image[y:h, x:w].copy()

kernel = np.ones((6,6),np.float32)/25
dst = cv2.filter2D(dst_roi,-1,kernel)

gray_image = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 100, param1=60, param2=40, minRadius=5, maxRadius=60)
if circles is not None:
    circles = circles[0, :].astype("int")

    for (x, y, radius) in circles:
        cv2.circle(dst_roi, (x, y), radius, (0, 255, 0), 4)
        dst_hit = dst[(y - 10):(y + 10), (x - 10):(x + 10)].copy()

    #cv2.imshow("image", image)
    #cv2.imshow("dst", dst)
    #cv2.imshow("gray_image", gray_image)
    #cv2.imshow("dst_roi", dst_roi)
    #cv2.imshow("dst_hit", dst_hit)
    #cv2.waitKey(0)
else:
    print("원이 검출되지 않음")

hsvFrame = cv2.cvtColor(dst_hit, cv2.COLOR_BGR2HSV)

red_lower = np.array([159, 50, 70], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

green_lower = np.array([36, 50, 70], np.uint8)
green_upper = np.array([89, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

yellow_lower = np.array([25, 50, 70], np.uint8)
yellow_upper = np.array([35, 255, 255], np.uint8)
yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

kernal = np.ones((5, 5), "uint8")

red_mask = cv2.dilate(red_mask, kernal)
res_red = cv2.bitwise_and(dst_hit, dst_hit, mask=red_mask)

green_mask = cv2.dilate(green_mask, kernal)
res_green = cv2.bitwise_and(dst_hit, dst_hit, mask = green_mask)

yellow_mask = cv2.dilate(yellow_mask, kernal)
res_yellow = cv2.bitwise_and(dst_hit, dst_hit, mask = yellow_mask)

contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 10):
        result = cv2.imread("result_r.jpg")
        cv2.putText(dst_roi, "Red", (x-20, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 10):
        result = cv2.imread("result_g.jpg")
        cv2.putText(dst_roi, "Green", (x - 20, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if (area > 10):
        result = cv2.imread("result_y.jpg")
        cv2.putText(dst_roi, "Yellow", (x - 20, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))

plt.figure(figsize=(10,5))
plt.subplot(131)
plt.axis('off')
plt.title('Filter2D')
plt.imshow(dst[:, :, [2, 1, 0]])
plt.subplot(132)
plt.axis('off')
plt.title('HoughCircles')
plt.imshow(dst_roi[:, :, [2, 1, 0]])
plt.subplot(133)
plt.axis('off')
plt.title('Color Detection')
plt.imshow(result[:, :, [2, 1, 0]])

plt.tight_layout()
plt.show()