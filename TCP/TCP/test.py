class Teacher(object):
    def __init__(self, name):
        self.name = name

    def shuxue(self):
        print(f'{self.name}数学')

    def _yuwen(self):
        print(f'{self.name}语文')

    def __yingyu(self):
        print(f'{self.name}英语')


class Tea(Teacher):
    def show(self):
        super(Tea, self).shuxue()
        super(Tea, self)._yuwen()
        # super(Tea, self).__yingyu()  子类不能调用__的方法

    def _yuwen(self):
        super(Tea, self)._yuwen()
        print('Tea的语文')

