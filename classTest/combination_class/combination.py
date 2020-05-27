class Person:

    def __init__(self,name,age,gender,birthday,address,contact):
        self.name=name
        self.age=age
        self.gender=gender
        self.birthday=birthday
        self.address=address
        self.contact=contact

    def printBascInformation(self):
        print("姓名：{},age:{},gender:{}".format(self.name,self.age,self.gender))

    def printBirthdayInformation(self):
        print("生日：%s年%s月%s日"%(self.birthday.year,self.birthday.month,self.birthday.day))

    def printAllInformation(self):
        self.printBascInformation()
        self.printBirthdayInformation()
        self.address.printAddressInformation()
        self.contact.\
            printContactInformation()


class Birthday:

    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day


class Address:

    def __init__(self,nation,province,city):
        self.nation=nation
        self.province=province
        self.city=city

    def printAddressInformation(self):
        print("地址：%s,%s,%s"%(self.nation,self.province,self.city))

class Contact:

    def __init__(self,phone,qq):
        self.phone=phone
        self.qq=qq

    def printContactInformation(self):
        print("联系方式：电话 {},qq {}".format(self.phone,self.qq))

birthday=Birthday("1996","05","17")
address=Address("中国","湖北",'武汉')
contact=Contact("15549080517","1143908462")

person=Person("guoqin",18,"男",birthday,address,contact)

person.printAllInformation()