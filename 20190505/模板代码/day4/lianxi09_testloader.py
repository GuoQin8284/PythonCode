
# 加载器实现 -- 向测试套件中添加测试用例
# 1. 实例化加载器对象TestLoader()
#    1. loader   =  unittest.TestLoader()
#    2. unittest.defaultTestLoader
# 2. 加载器对象调用discover()
#    1. 调用--加载器对象调用
#       参数--指定的目录,指定文件名
#       返回--添加好测试用例的套件对象
#    2. loader.discover("用例文件目录",pattern="test*.py")


# suite = unittest.defaultTestLoader.discover(start_dir="./case/",pattern="test*.py")



# 运行测试套件  借助于TestTestRunner
# a.实例化运行器对象

# b.运行器对象调用run方法
