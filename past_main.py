import cv2
from PoseModule import PoseDetector

cap1=cv2.VideoCapture('biceps3.mov')
cap2=cv2.VideoCapture(0)

video_detector=PoseDetector()
webcam_detector=PoseDetector()
posList=[]

while True:
    ret,frame1=cap1.read()
    _, frame2=cap2.read()

    #아래 코드를 위로 가져와서 프레임 사이즈 변환 먼저 함
    frame1 = cv2.resize(frame1, (640, 360))
    frame2 = cv2.resize(frame2, (640, 360))

    if not ret:
        print('가져올 프레임 없음')
        break

    frame1=video_detector.findPose(frame1,draw=True)
    lmList1=video_detector.findPosition(frame1)
    print(lmList1)

    try:
        x11, y11=lmList1[11][1:]
        x12, y12=lmList1[12][1:]
        x13, y13=lmList1[13][1:]
        x14, y14=lmList1[14][1:]
        x15, y15=lmList1[15][1:]
        x16, y16=lmList1[16][1:]
        x23, y23=lmList1[23][1:]
        x24, y24=lmList1[24][1:]
        x25, y25=lmList1[25][1:]
        x26, y26=lmList1[26][1:]
        x27, y27=lmList1[27][1:]
        x28, y28=lmList1[28][1:]
    except Exception as e:
        pass


    # for i in range(11,17):
    #     globals()['x{}'.format(i)]=lmList1[i][1]
    #     globals()['y{}'.format(i)]=lmList1[i][2]
    # for i in range(23,29):
    #     globals()['x{}'.format(i)]=lmList1[i][1]
    #     globals()['y{}'.format(i)]=lmList1[i][2]

    #print(lmList1[12])

    frame2=webcam_detector.findPose(frame2)
    lmList2=webcam_detector.findPosition(frame2)
    # a11, b11=lmList2[11][1:]
    # a12, b12=lmList2[12][1:]
    # a13, b13=lmList2[13][1:]
    # a14, b14=lmList2[14][1:]
    # a15, b15=lmList2[15][1:]
    # a16, b16=lmList2[16][1:]
    # a23, b23=lmList2[23][1:]
    # a24, b24=lmList2[24][1:]
    # a25, b25=lmList2[25][1:]
    # a26, b26=lmList2[26][1:]
    # a27, b27=lmList2[27][1:]
    # a28, b28=lmList2[28][1:]

    cv2.line(frame2, (x11, y11), (x13, y13), (255, 255, 255), 3)
    cv2.line(frame2, (x13, y13), (x15, y15), (255, 255, 255), 3)
    cv2.line(frame2, (x12, y12), (x14, y14), (255, 255, 255), 3)
    cv2.line(frame2, (x14, y14), (x16, y16), (255, 255, 255), 3)
    cv2.line(frame2, (x11, y11), (x12, y12), (255, 255, 255), 3)
    cv2.line(frame2, (x23, y23), (x24, y24), (255, 255, 255), 3)
    cv2.line(frame2, (x24, y24), (x26, y26), (255, 255, 255), 3)
    cv2.line(frame2, (x26, y26), (x28, y28), (255, 255, 255), 3)
    cv2.line(frame2, (x23, y23), (x25, y25), (255, 255, 255), 3)
    cv2.line(frame2, (x25, y25), (x27, y27), (255, 255, 255), 3)
    cv2.line(frame2, (x12, y12), (x24, y24), (255, 255, 255), 3)
    cv2.line(frame2, (x11, y11), (x23, y23), (255, 255, 255), 3)
    cv2.line(frame2, (x23, y23), (x24, y24), (255, 255, 255), 3)

    # length1=math.hypot(x11-x12,y11-y12)
    # length2=math.hypot(a11-a12,b11-b12)
    # k=length1/length2
    # p14, q14 = int(a12-k*(x12-x14)), int(b12-k*(y12-y14))
    # p16, q16 = int(a12-k*(x12-x16)), int(b12-k*(y12-y16))
    #
    # cv2.line(frame2, (x11, y11), (x13, y13), (255, 255, 255), 3)
    # cv2.line(frame2, (x13, y13), (x15, y15), (255, 255, 255), 3)
    # cv2.line(frame2, (a12, a12), (p14, q14), (255, 255, 255), 3)
    # cv2.line(frame2, (p14, q14), (p16, q16), (255, 255, 255), 3)

    #print('2',lmList2)


    print(frame2.shape)

    #print(frame1.shape, frame2.shape)

    cv2.imshow('video1',frame1)
    cv2.imshow('video2',frame2)

    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료')
        break

cap1.release()
