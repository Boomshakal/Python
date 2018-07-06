import _thread
import  time

def loop1():
    print("start loop1 at:",time.ctime())
    time.sleep(4)
    print("end loop1 at:",time.ctime())


def loop2():
    print("start loop2  at:",time.ctime())
    time.sleep(2)
    print("end loop2 at:",time.ctime())

def main():
    print("starting at:",time.ctime())
    loop1()
    loop2()
    print("all done at:",time.ctime())

if __name__ == '__main__':
    main()