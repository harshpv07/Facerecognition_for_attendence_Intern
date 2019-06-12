def threadd():
    import threading
    from temp2 import findface
    from motion_detection import motion
    t1  = threading.Thread(target=findface)
    t2 = threading.Thread(target=motion)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == '__main__':
    threadd()
    