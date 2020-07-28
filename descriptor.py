# 描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()中的一个,这也被称为描述符协议。

class Str:
    def __get__(self, instance, owner):
        print("Str调用")
    def __set__(self, instance, value):
        print("Str设置")
    def __delete__(self, instance):
        print("Str删除")

class Int:
    def __get__(self, instance, owner):
        print("Int调用")
    def __set__(self, instance, value):
        print("Int设置")
    def __delete__(self, instance):
        print("Int删除")
class People:
    name = Str()
    age = Int()
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = People('alex',18)

# 描述符Str的使用
p1.name
p1.name = 'egon'
del p1.name

# 描述符Int 的使用
p1.age
p1.age = 18
del p1.age

#
print(p1.__dict__)
print(People.__dict__)

# 描述符本身应该定义成新式类,被代理的类也应该是新式
# 类必须把描述符定义成这个类的类属性，不能为定义到构造函数中
# 要严格遵循优先级,优先级由高到底分别是：1.类属性；2.数据描述符；3.实例属性；4.非数据描述符；5.找不到的属性触发__getattr__()

# 使用
class Str:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Str('name')
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

p1=People('egon',18,3231.3)

#调用
print(p1.__dict__)
p1.name
"""
set---> <__main__.People object at 0x10402cba8> egon
{'name': 'egon', 'age': 18, 'salary': 3231.3}
get---> <__main__.People object at 0x10402cba8> <class '__main__.People'>
"""

#赋值
print(p1.__dict__)
p1.name='egonlin'
print(p1.__dict__)
"""
{'name': 'egon', 'age': 18, 'salary': 3231.3}
set---> <__main__.People object at 0x10402cc18> egonlin
{'name': 'egonlin', 'age': 18, 'salary': 3231.3}
"""

#删除
print(p1.__dict__)
del p1.name
print(p1.__dict__)
"""
{'name': 'egonlin', 'age': 18, 'salary': 3231.3}
delete---> <__main__.People object at 0x10402cba8>
{'age': 18, 'salary': 3231.3}
"""


