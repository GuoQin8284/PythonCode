class Student:
    baseClassData=123
    def __init__(self,num,name,gender):
        self.num=num
        self.name=name
        self.gender=gender

    def printInformation(self):
        print("num:{},name:{},gender:{}".format(self.num,self.name,self.gender))


class Student1(Student):
    def __init__(self,num,name,gender,age,address):
        Student.__init__(self,num,name,gender)
        self.age=age
        self.address=address

    def printInformation1(self):
        Student.printInformation(self)
        print("age:{},address:{}".format(self.age,self.address))

s=Student1(100,"xiaoli","nv","18","wuhan")
s.printInformation1()
print("s.baseClassData={}".format(s.baseClassData))