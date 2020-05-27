class Person(object):
    def name(self,name):
        self.name=name
        print(self.name)
    def eat(self):
        print('吃饭')
    def sleep(self):
        print('在家睡觉')
class Student(Person):
    def stduy(self):
        print('学习')

    def sleep(self,is_athome):
        if is_athome:
            super().sleep()
        else:
            print('在教室睡觉')

xiaoming=Student()
xiaoming.name('小明')
xiaoming.eat()
xiaoming.sleep('')
xiaoming.stduy()
