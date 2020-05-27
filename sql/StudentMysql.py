import pymysql

class StuMysql:

    CreateUesr="insert info student values"

    # 创建数据库链接对象
    def __init__(self,name,pwd):
        self.cn1=pymysql.connect("127.0.0.1",name,pwd)
        self.cursor=self.cn1.cursor()

    # 执行sql命令方法
    def execute(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 输出查询信息
    def PrintInfo(self,select_sql):
        print(self.execute(select_sql))

    def SelectAllUser(self):
        self.selectAllUser="select * from student"
        return self.selectAllUser

    def Create_db(self,sqlName):
        self.create_db = "create database is not exists {} character set utf8".format(sqlName)
        return self.create_db

    def UpdateUserInfo(self,oldName,newName):
        self.updateUser="update student set name={} where name={}".format(newName,oldName)
        return self.updateUser

    def SelectUser(self,name):
        self.selectUser="select * from where name={}".format(name)
        return self.selectUser

    def DeleteUser(self,name):
        self.deleteUser="delete from student where name={}".format(name)
        return self.deleteUser

    def Find_stu(self,name):
        if len(self.SelectUser(name)):
            return 1
        else:
            return 0
