# super重载
# class supper:
#     def __init__(self,a):
#         self.supper_data=a
#
# class sub(supper):
#     def __init__(self,a,b):
#         self.sub_data=a
#         super(sub,self).__init__(b)
#
# x=sub(10,20)
# print(x.supper_data)
# print(x.sub_data)
# print(x.__init__(4,5))
# print(x.sub_data)
# print(x.supper_data)

# 子类定义的属性和方法与父类重名时，方法重载
# class supper:
#     data1=10
#     data2=20
#     def show1(self):
#         print("在父类的show1方法中的输出")
#
#     def show2(self):
#         print("在父类的show2方法中的输出")
#
# class sub(supper):
#     data1=100
#     def show1(self):
#         print("在子类的show1方法中的输出")
#
# x=sub()
# print(x.data1,x.data2)
# x.show1()
# x.show2()


# 多重继承
# class P1:
#     def f(self):
#         print("P1的f方法被调用")
#
# class P2:
#     def f(self):
#         print("P2的f方法被调用")
#
#     def h(self):
#         print("P2的h方法被调用")
#
# class C1(P1,P2):
#     def m(self):
#         print("C1的m方法被调用")
# class C2(P1,P2):
#     def h(self):
#         print("C2的h方法被调用")
# class C3(C1,C2):
#     def c(self):
#         print("C3的c方法被调用")
# x=C3()
# x.c()
# x.f()
# x.h()

# 基类同名方法参数个数相同的情况
# class A:
#     def __init__(self,a):
#         self.a=a
#         print("A.a={}".format(self.a))
#
# class B:
#     def __init__(self,b):
#         self.b=b
#         print("B.b={}".format(self.b))
#
# class C(A,B):
#     def __init__(self,a,b):
#         super(C,self).__init__(a)
#         super(C,self).__init__(b)
#         print("C类的__init__方法被调用")
#
# x=C(10,20)
# print(x.a)
# print(x.b)

# 基类同名方法参数不同的情况
class A:
    def __init__(self,a):
        self.a=a
        print("A.a=%d"%self.a)

class B:
    def __init__(self):
        # self.a=a
        # self.b=b
        # print("B.a=%d"%self.a)
        # print("B.b=%d"%self.b)
        print("B的__init方法被调用")
class C(A,B):
    def __init__(self,a):
        super(C,self).__init__(a)
        super(C,self).__init__()

x=C(10)