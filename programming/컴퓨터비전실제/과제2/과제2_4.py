import cv2
import numpy as np

img0 = cv2.imread('stitching/dog_a.jpg', cv2.IMREAD_COLOR)
img0 = cv2.resize(img0, None, fx=0.5, fy=0.5)
img1 = cv2.imread('stitching/dog_b.jpg', cv2.IMREAD_COLOR)
img1 = cv2.resize(img1, None, fx=0.5, fy=0.5)

img0_1 = np.copy(img0)
img1_1 = np.copy(img1)
img0_2 = np.copy(img0)
img1_2 = np.copy(img1)
img0_3 = np.copy(img0)
img1_3 = np.copy(img1)

prev_pts = None
prev_gray_frame = None
tracks = None

frame = img0_1

while True:
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_pts is not None:
        pts, status, errors = cv2.calcOpticalFlowPyrLK(
            prev_gray_frame, gray_frame, prev_pts, None, winSize=(15, 15), maxLevel=5,
            criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
        good_pts = pts[status == 1]
        if tracks is None:
            tracks = good_pts
        else: tracks = np.vstack((tracks, good_pts))
        for p in tracks:
            cv2.circle(frame, (int(p[0]), int(p[1])), 3, (0, 255, 0), -1)

    else:
        pts = cv2.goodFeaturesToTrack(gray_frame, 500, 0.05, 10)
        pts = pts.reshape(-1, 1, 2)

    prev_pts = pts
    prev_gray_frame = gray_frame

    cv2.imshow('frame', frame)


    key = cv2.waitKey() & 0xff
    if key == 27: break

    frame = img1_1

cv2.destroyAllWindows()

def display_flow(img, flow, stride=40):
    for index in np.ndindex(flow[::stride, ::stride].shape[:2]):
        pt1 = tuple(i*stride for i in index)
        delta = flow[pt1].astype(np.int32)[::-1]
        pt2 = tuple(pt1 + 10*delta)
        if 2 <= cv2.norm(delta) <= 10:
            cv2.arrowedLine(img, pt1[::-1], pt2[::-1],
                                (0,0,255), 5, cv2.LINE_AA, 0, 0.4)

    norm_opt_flow = np.linalg.norm(flow, axis=2)
    norm_opt_flow = cv2.normalize(norm_opt_flow, None, 0, 1,
                                  cv2.NORM_MINMAX)

    cv2.imshow('optical flow', img)
    cv2.imshow('optical flow magnitude', norm_opt_flow)
    k = cv2.waitKey(1)

    if k == 27:
        return 1
    else:
        return 0

prev_frame = cv2.cvtColor(img0_2, cv2.COLOR_BGR2GRAY)
frame = img1_2
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

opt_flow = cv2.calcOpticalFlowFarneback(prev_frame, gray, None, 0.5, 5,  13, 10,
                                                5, 1.1, cv2.OPTFLOW_FARNEBACK_GAUSSIAN)

display_flow(frame, opt_flow)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

prev_frame = cv2.cvtColor(img0_2, cv2.COLOR_BGR2GRAY)
frame = img1_2
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

flow_DualTVL1 = cv2.createOptFlow_DualTVL1()

opt_flow = flow_DualTVL1.calc(prev_frame, gray, None)
flow_DualTVL1.setUseInitialFlow(True)

prev_frame = np.copy(gray)
display_flow(frame, opt_flow)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()