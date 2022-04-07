import time

import cv2

from PoseModule import PoseDetector

import sys
sys.path.append("./tubePose.py")
from tubePose import x, y, drawline, lmList1


def camPose():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = PoseDetector()



    while True:
        success, img2 = cap.read()
        img2 = cv2.flip(img2, 1)
        img2 = cv2.resize(img2, (640, 400))
        #사용자가 보기 편하게 좌우 반전
        img2 = detector.findPose(img2)
        lmList2=detector.findPosition(img2,draw=False)
        if len(lmList2) !=0:
            print(lmList2[14])
            cv2.circle(img2, (lmList2[14][1], lmList2[14][2]), 15, (0,0,255), cv2.FILLED)

        # 라인을 표시하려 하면 x, y의 범위가 초과되어 오류가 발생
        # drawline(lmList1)
        # for i in range(11, 15):
        #     cv2.line(img2, (x[i], y[i]), (x[i+2], y[i+2]), (255, 255, 255), 3)
        #     # cv2.line(img2, (x11, y11), (x13, y13), (255, 255, 255), 3)
        #     # cv2.line(img2, (x13, y13), (x15, y15), (255, 255, 255), 3)
        #     # cv2.line(img2, (x12, y12), (x14, y14), (255, 255, 255), 3)
        #     # cv2.line(img2, (x14, y14), (x16, y16), (255, 255, 255), 3)
        #
        # lines=[11, 23]
        # for line in lines:
        #     cv2.line(img2, (x[line], y[line]), (x[line+1], y[line+1]), (255, 255, 255), 3)
        #     # cv2.line(img2, (x11, y11), (x12, y12), (255, 255, 255), 3)
        #     # cv2.line(img2, (x23, y23), (x24, y24), (255, 255, 255), 3)
        # for i in range(23, 27):
        #     cv2.line(img2, (x[i], y[i]), (x[i+2], y[i+2]), (255, 255, 255), 3)
        # # cv2.line(img2, (x24, y24), (x26, y26), (255, 255, 255), 3)
        # # cv2.line(img2, (x26, y26), (x28, y28), (255, 255, 255), 3)
        # # cv2.line(img2, (x23, y23), (x25, y25), (255, 255, 255), 3)
        # # cv2.line(img2, (x25, y25), (x27, y27), (255, 255, 255), 3)
        #
        # for i in range(11, 13):
        #     cv2.line(img2, (x[line], y[line]), (x[line + 12], y[line + 12]), (255, 255, 255), 3)
        # # cv2.line(img2, (x12, y12), (x24, y24), (255, 255, 255), 3)
        # # cv2.line(img2, (x11, y11), (x23, y23), (255, 255, 255), 3)
        #
        # # cv2.line(img2, (x23, y23), (x24, y24), (255, 255, 255), 3)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        #cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    #(255, 0, 0), 3)
        cv2.imshow('camPose', img2)
        if cv2.waitKey(1) == ord('q'):
            break
