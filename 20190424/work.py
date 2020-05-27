"""
1.	定义一个Employee类：
def __init__(self, name, job = None, pay = 0):
		pass
#加薪的方法， percent为加薪比例，可能为0.1
	def giveraise(self, percent):
		pass
	def __str__(self):
    		return '[Person: %s, %d]' % ( self.name, self.pay)
再定义一个Manager类，实现其中的giveraise()方法，对于Manager来说，除了percent的固定加薪外，还要额外奖励bonus：
	def giveraise(self, percent, bonus = 0.1):
	pass
"""
class Person(object):
    def work(self,work):
        self.work=work
        print(self.work)
class Empolyee(Person):
    def __init__(self,name,job,pay):
        self.name=name
        self.job=job
        self.pay=pay
    def giveraise(self,percent):
        self.percent=percent
        self.pay *=(percent+1)
    # def __str__(self):
        # return '[Person: %s,职位：%s, 工资%d]'%(self.name,self.job, self.pay)
    def work(self):
        print('员工工作')
class Manager(object):
    def giveraise(self, percent, bonus=0.1):
        pass

class Stu(Person):
    __count=50
    @classmethod
    def stu_count(cls):
        print('当前学生人数为：',cls.__count)
    def __init__(self,name):
        self.name=name
    def stu_work(self):
        print('%s是学生在实习'% self.name)
        Stu.__count -= 1
    def __str__(self):
        return self.name

class Company(object):
    def do_work(self,who):
        self.who=who
        print(self.who)

xiaoming=Empolyee("小明","保安",3000)
daming=Stu("大明")
daming.stu_work()
daming.stu_count()
baoan=Company()
baoan.do_work(daming)
# print(xiaoming)


