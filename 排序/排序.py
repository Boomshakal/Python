from itertools import chain
import operator
import datetime

a = [1, 4, 5, 12]
b = [35, 76, 11, 34]

print(sorted(chain(a, b)))


class UserInfo(object):

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}-{self.age}-{self.birthday}"

    def __repr__(self):
        return f"{self.name}-{self.age}-{self.birthday}"


user1 = UserInfo('li', 28, datetime.date(1991, 10, 16))
user2 = UserInfo('min', 30, datetime.date(1989, 9, 17))
user3 = UserInfo('cong', 29, datetime.date(1990, 12, 6))

user_list = [user1, user2, user3]

def month(obj):
    return obj.birthday.month

print(sorted(user_list, key=operator.attrgetter("birthday.year")))
print(sorted(user_list, key=month))

dict_list = [{'name': 'li', 'age': 28, 'birthday': datetime.date(1991, 10, 16)},
             {'name': 'min', 'age': 30, 'birthday': datetime.date(1989, 9, 17)},
             {'name': 'cong', 'age': 29, 'birthday': datetime.date(1990, 12, 6)}]

print(sorted(dict_list, key=lambda item:item['age']))
print(sorted(dict_list, key=operator.itemgetter('age')))
