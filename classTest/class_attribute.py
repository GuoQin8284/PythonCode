
# 公私有属性
# class Test:
#     name="张三"
#     age=20
#     __hight=170
#     def __init__(self,city,nation,job):
#         self.city=city
#         self.nation=nation
#         self.__job=job
# p1=Test("武汉",'中国',"程序员")
#
# print('通过类访问类公有属性：name={},age={}'.format(Test.name,Test.age))
# print('通过类访问类私有属性：hight={}'.format(Test._Test__hight))
# print("通过实例对象访问类公有属性：name={},age={}".format(p1.name,p1.age))
# print("通过实例对象访问类私有属性：hight={}".format(p1._Test__hight))
# print("通过实例对象访问对象公有属性：city={},nation={}".format(p1.city,p1.nation))
# print("通过实例对象访问对象私有属性：job={}".format(p1._Test__job))
# print("通过类访问对象属性：city={},nation={}".format(Test.city,Test.nation))


# 公私有方法
# class TestMethon():
#     def PublicMethon(self):
#         return "公有方法PublicMethon"
#     def __privateMethon(self):
#         return "私有方法PrivateMethon"
#
# m=TestMethon()
# print("通过类调用",TestMethon.PublicMethon(m))
# print("通过类调用",TestMethon._TestMethon__privateMethon(m))
# print("通过实例对象调用",m.PublicMethon())
# print("通过实例对象调用",m._TestMethon__privateMethon())

# 类方法和静态方法

# class Methods():
#     # 定义一个公有类方法
#     @classmethod
#     def PublicClassMethod(cls):
#         return '公有类方法'
#
#     # 定义一个私有类方法
#     @classmethod
#     def __PrivateClassMethod(cls):
#         return "私有类方法"
#
#     # 定义一个公有静态方法
#     @staticmethod
#     def StaticPublicMethod():
#         return "公有静态方法"
#
#     # 定义一个私有静态方法
#     @staticmethod
#     def __StaticPrivateMethod():
#         return "私有静态方法"
#
#     # 定义一个公有对象方法
#     def PublicMethon(self,content="共有对象"):
#         return "{}方法".format(content)
#
#     # 定义一个私有方法
#     def __PrivateMethod(self,content="私有对象"):
#         return "{}方法".format(content)
#
#     # 使用内置函数将公有对象方法转换为公有类方法
#     a = classmethod(PublicMethon)
#
#     # 使用内置函数将私有对象方法转换为私有类方法
#     a1 = classmethod(__PrivateMethod)
#
#     # 使用内置函数将公有对象方法转换为公有静态方法
#     b = staticmethod(PublicMethon)
#
#     # 使用内置函数将私有对象方法转换为私有静态方法
#     b1 = staticmethod(__PrivateMethod)
# m = Methods()
# print("以对象调用",m.PublicClassMethod())
# print("以对象调用",m._Methods__PrivateClassMethod())
# print("以对象调用",m.StaticPublicMethod())
# print("以对象调用",m._Methods__StaticPrivateMethod())
# print("以对象调用",m.PublicMethon())
# print("以对象调用",m._Methods__PrivateMethod())
# print("以对象调用",m.a("通过内建函数转换为类公有"))
# print("以对象调用",m.a1("通过内建函数转换为类私有"))
# print("以对象调用",m.b("通过内建函数转换为公有静态"))
# print("以对象调用",m.b1("通过内建函数转换为私有静态"))
# print("以类调用",Methods.PublicClassMethod())
# print("以类调用",Methods._Methods__PrivateClassMethod())
# print("以类调用",Methods.StaticPublicMethod())
# print("以类调用",Methods._Methods__StaticPrivateMethod())
# print("以类调用",Methods.PublicMethon(m))
# print("以类调用",Methods._Methods__PrivateMethod(m))
# print("以类调用",Methods.a("通过内建函数转换为类公有"))
# print("以类调用",Methods.a1("通过内建函数转换为类私有"))
# print("以类调用",Methods.b("通过内建函数转换为公有静态"))
# print("以类调用",Methods.b1("通过内建函数转换为私有静态"))
# print("dir",dir(Methods))

# 构造方法和析构方法
# class Methods():
#
#     def __init__(self,value):
#         self.value=value
#         print("构造方法加载完毕")
#
#     def __del__(self):
#         del self.value
#         print("析构函数执行完毕")
#
# m=Methods(100)
# print(m.value)
# del m


class Test:
    age=100
    data=10
    def __init__(self,data,name):
        self.data=data
        self.name=name

xiaoMing=Test("20","小明")

print("Test.age={}".format(Test.age))
print("xiaoMing",xiaoMing.data)
