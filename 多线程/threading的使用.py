import threading
import time

def loop1(a):
    print("start loop1 at:",time.ctime(),a)
    time.sleep(4)
    print("end loop1 at:",time.ctime())


def loop2(b):
    print("start loop2  at:",time.ctime(),b)
    time.sleep(2)
    print("end loop2 at:",time.ctime())

def main():
    print("starting at:",time.ctime())
    t1=threading.Thread(target=loop1,args=("我是天才",))
    t1.start()
    t2=threading.Thread(target=loop2,args=("我是人才",))
    t2.start()
    t1.join()  #等待线程执行完毕
    t2.join()

    print("all done at:",time.ctime())

if __name__ == '__main__':
    main()