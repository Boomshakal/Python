#定义一个空的类
class Student():
    pass

#定义个对象
xiaoming=Student()

#在定义一个类，可以描述听Python的学生
class PythonStudent():
    def __init__(self):
        self.name = None
        self.age = 18
        self.score="Python"

    def doHomework(self):
        print("I 在做作业")

        return None


       #魔法函数 call自己被调用成函数
    def __call__(self, *args, **kwargs):
        print("我当函数用了")
    def __str__(self):
        return "我当字符串用了"
    def __setattr__(self, key, value):
        print("设置属性：{0}".format(key))

#实体化一个叫月月的学生，是个具体的人

yueyue=PythonStudent()
yueyue.doHomework()
yueyue.age=19
#yueyue()
print(yueyue)
