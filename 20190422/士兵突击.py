class Gun(object):
    def __init__(self,model):
        self.model=model
        self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count += count
        print('当前子弹：%s'% self.bullet_count)
    def shoot(self):
        if self.bullet_count==0:
            print('没子弹啦')
        print('射击')
        for a in range(self.bullet_count):
            self.bullet_count -= 1
            print(self.bullet_count)

class Soldier(object):
    def __init__(self,name,gun):
        self.name=name
        self.gun=gun
    def fire(self):
        if self.gun==None:
            print('%s 还没有枪'%self.name)
        print('%s 有%s了'%(self.name,self.gun.model))
        self.gun.add_bullet(50)

qiang = Gun('ak47')
xsd=Soldier('许三多',qiang)
xsd.fire()
qiang.shoot()