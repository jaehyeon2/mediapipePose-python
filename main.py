from multiprocessing import Process

from tubePose import tubePose
from camPose import camPose


if __name__=='__main__':

    video=Process(target=tubePose)
    video.start()

    cam = Process(target=camPose)
    cam.start()

    video.join()
    cam.join()