from multiprocessing import Process, Manager

from tube_pose import tube_pose
from cam_pose import cam_pose


if __name__ == '__main__':
    manager = Manager()
    shared_dict = manager.dict()  # 프로세스 간 공유되는 객체

    video = Process(target=tube_pose, args=(shared_dict,))
    video.start()

    cam = Process(target=cam_pose, args=(shared_dict,))
    cam.start()


    video.join()
    cam.join()