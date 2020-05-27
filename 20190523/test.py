class Cat():
    def drink(self):
        print("%s爱吃鱼"% self.name)

    def eat(self):
        print("%s爱喝水"% self.name)


xiaohua=Cat()
xiaohua.name="小花"
xiaohua.drink()
xiaohua.eat()

print(id(xiaohua))

