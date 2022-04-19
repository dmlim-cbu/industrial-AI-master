import cv2
#import matplotlib.pyplot as plt
import numpy as np

keyin = 0

while cv2.waitKey(2000) < 0:
    if keyin == 0:
        image = cv2.imread("sigb_r.jpg")
    elif keyin == 1:
        image = cv2.imread("sigb_g.jpg")
    elif keyin == 2:
        image = cv2.imread("sigb_y.jpg")

    #print("image : ", image.shape)

    cv2.rectangle(image, (440, 150), (900, 450), (0, 255, 0), 2)
    cv2.imshow("image", cv2.resize(image, None, fx=0.5, fy=0.5))

    dst_roi = image[150:450, 440:900].copy()

    kernel = np.ones((6, 6), np.float32) / 25
    dst = cv2.filter2D(dst_roi, -1, kernel)

    gray_image = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 100, param1=60, param2=40, minRadius=5,
                               maxRadius=60)
    if circles is not None:
        circles = circles[0, :].astype("int")

        for (x, y, radius) in circles:
            cv2.circle(dst_roi, (x, y), radius, (0, 255, 0), 4)
            dst_hit = dst[(y - 10):(y + 10), (x - 10):(x + 10)].copy()

        cv2.imshow("HoughCircles", dst_roi)
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
    res_green = cv2.bitwise_and(dst_hit, dst_hit, mask=green_mask)

    yellow_mask = cv2.dilate(yellow_mask, kernal)
    res_yellow = cv2.bitwise_and(dst_hit, dst_hit, mask=yellow_mask)

    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 10):
            result = cv2.imread("result_r.jpg")
            cv2.putText(dst_roi, "Red", (x - 20, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

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

    cv2.imshow("filter2D", gray_image)
    cv2.imshow("dst_hit", dst_hit)
    cv2.imshow("Color Detect (findContours)", dst_roi)
    cv2.imshow("result", result)

    keyin += 1
    if keyin == 3: keyin = 0

cv2.destroyAllWindows()