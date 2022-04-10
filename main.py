from multiprocessing import Process, Manager

from tubePose import tubePose
from camPose import camPose


if __name__=='__main__':
    manager = Manager()
    shared_dict = manager.dict()

    video=Process(target=tubePose, args=(shared_dict, ))
    video.start()

    cam = Process(target=camPose, args=(shared_dict, ))
    cam.start()

    video.join()
    cam.join()