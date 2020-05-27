class Person(object):
    def __init__(self,name,age,gender,nation):
        self.name=name
        self.age=age
        self.gender=gender
        self.nation=nation
        print(id(self.age))

    def setName(self,name):
        self.name=name

    def setAge(self,age):
        self.age=age
        print("setAge",id(self.age))

    def setGender(self,gender):
        self.gerder=gender

    def setNation(self,nation):
        self.nation=nation

    def getName(self):
        return self.name

    def getAge(self):
        print("getAge:",id(self.age))
        return self.age

    def getGender(self):
        return self.gender

    def getNation(self):
        return self.nation

    def printMessage(self):
        print("printAge:",id(self.age))
        return "姓名：{},性别：{},年龄：{},国籍：{}".format(self.name,self.gender,self.age,self.nation)

chinesePerson=Person("张三","20","男","中国")

americanPerson=Person("Lucy","21","女","美国")

germanPerson=Person("Pander","22","男","德国")

print("chinesePerson对象信息：",chinesePerson.printMessage())
print("americanPerson对象信息：",americanPerson.printMessage())
print("germanPerson对象信息：",germanPerson.printMessage())

chinesePerson.setAge(25)
print("chinesePerson对象age属性值为：",chinesePerson.getAge())

chinesePerson.age=29
print("chinesePerson对象age属性值为：",chinesePerson.getAge())

print(id(chinesePerson.age))