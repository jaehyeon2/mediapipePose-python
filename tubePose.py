# import time

import cv2
from cv2 import CAP_PROP_FPS

from PoseModule import PoseDetector

lmList1=[]
x=[]
y=[]
def tubePose():
    cap = cv2.VideoCapture('biceps3.mov')
    detector = PoseDetector()
    videofps=cap.get(CAP_PROP_FPS)
    print("fps -> ", videofps)
    delay=round(1000/videofps)

    posList = []

    while True:
        success, img1 = cap.read()
        img1 = cv2.resize(img1, (640,400))

        if not success:
            print('가져올 프레임 없음')
            break

        img1 = detector.findPose(img1)
        lmList1 = detector.findPosition(img1, draw=False)
        print(lmList1)

        lmString = ''
        for lm in lmList1:
            lmString += f'{lm[1]}, {lm[2]},'
        posList.append(lmString)

        # cTime = time.time()
        # fps = videofps
        # pTime = cTime

        # cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
        # (255, 0, 0), 5)


        cv2.imshow('videoPose', img1)
        if (cv2.waitKey(delay)==27)|(cv2.waitKey(1)==ord('q')):
            break
        # if key == ord('s'):
        #with open("/Users/ming/PycharmProjects/pythonProject/2Dposition.txt", 'w') as f:
        #    f.writelines(["%s\n" % item for item in posList])

def drawline(lmList1):
    try:
        for i in range(11, 29):
            x[i], y[i] = lmList1[i][1:]
    except Exception as e:
        pass