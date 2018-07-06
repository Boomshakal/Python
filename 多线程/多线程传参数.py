import _thread as thread
import  time

def loop1(a):
    print("start loop1 at:",time.ctime(),a)
    time.sleep(4)
    print("end loop1 at:",time.ctime(),a)


def loop2(b):
    print("start loop2  at:",time.ctime(),b)
    time.sleep(2)
    print("end loop2 at:",time.ctime(),b)

def main():
    print("starting at:",time.ctime())
    #参数两个，一个是需要运行的函数名，第二是函数的参数作为元祖使用，为空则使用空元祖
    thread.start_new_thread(loop1,("我是天才",))
    thread.start_new_thread(loop2,("我是人才",))
    print("all done at:",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)