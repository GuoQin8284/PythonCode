# def numm(m):
#     m=1
#     print('n:%d'%m)
# m = 100
# numm(m)
# print('m:%d'%m)

# class Student(object):
#     def study(self):
#         print('爱学习')
#     def run(self):
#         print('爱跑步')
# stu = Student()
# stu.run()
# stu.study()
#
# class stu ():
#     def __int__(self,name,height,weith):
#         self.name=name
#         self.height=height
#         self.weith=weith
#         print('name:%s'%self.name)
#         print('height:%s'%self.height)
#         print('weith:%s'%self.weith)
#         stu.stu_run()
#     def stu_run(self):
#         stu.study()
#         stu.run()
#     def study(self):
#         print('好好学习，天天向上')
#     def run(self):
#         print('健康工作50年')
# student=stu('haha','180','70kg')

class HouseItem(object):
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return "%s占地面积：%s"%(self.name,self.area)
class House(object):
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.free=area


    def add_item(self, item):
        self.item=item
        self.free = self.item - HouseItem.area
    def __str__(self):
        return '房间类型为:%s 房间总面积为:%s 房间剩余面积为:%s 家具名称:%s'%(self.house_type,self.area,self.free,bed.name)

bed=HouseItem('床',"4.5")
famliy=House('三室一厅','90')
print(bed)
print(famliy)
# hou=House('三室一厅','90')



