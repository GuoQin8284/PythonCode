class Master(object):
    def make_cake(self):
        print('传统方法制作煎饼果子')
class School(object):
    def make_cake(self):
        print('现代方法制作煎饼果子')
    def make_pizza(self):
        print('披萨')
class Prentice(Master,School):
    def __init__(self,name):
        self.name=name
    def make_cake(self):
        super(Prentice,self).make_cake()
        School.make_cake(self)
        print('独家秘方')
class Restrant(object):
    def __init__(self,name):
        self.name=name
    def cook(self,name):
        name.
        print('在%s做%s'%(self.name,self.food))

daming=Prentice('大明')
canguan=Restrant('和平饭店')
canguan.cook(daming.make_pizza())