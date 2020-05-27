from pickle import dump, load

from datetime import datetime

from StudentMysql import StuMysql

try:
    class User:
        def __init__(self,name=None,pwd=None):
            self.menu()
            self.mysql=StuMysql(name,pwd)

        # def find(self,name):
        #     global userlist
        #     n=-1
        #     for x in userlist:
        #         n += 1
        #         if x.name==name:
        #             break
        #     else:
        #         n=-1
        #     return n


        def menu(self):
            print("用户注册管理系统")
            print("\t 1.查找/修改/删除用户信息")
            print("\t 2.添加新用户")
            # print("\t 3.保存用户信息")
            print("\t 4.查看所有用户")
            print("\t 5.退出系统")
            action=input("请输入序号选择对应菜单：")
            if action=='1':
                self.updataUser()
            elif action=="2":
                self.addUser()
            # elif action=="3":
            #     self.save()
            elif action=="4":
                self.showAll()
            else:
                "系统已推出"

        def addUser(self,action="0"):
            global userlist
            while True:
                userName=input("请输入用户名：")
                index=self.mysql.Find_stu(userName)
                if userName=="":
                    print("用户名无效请重新输入")
                    continue
                elif index==1 and action=="0":
                    userPwd=input("请输入用户密码x:")
                    if userPwd=="":
                        print("请输入有效密码")
                    else:
                        print(userName, userPwd)
                        # print("User(userName,userPwd):%s"%User(userName,userPwd))
                        self.mysql.execute(self.mysql.Create_User(userName,userPwd))
                        print("用户信息已保存")
                        break
                elif index==0 and action=="1":
                    userPwd = input("请输入用户密码:")
                    if userPwd == "":
                        print("请输入有效密码")
                    else:
                        self.mysql.UpdateUserInfo(userName)
                        print("用户信息已修改")
                        break
                else:
                    print("用户名已存在")
                    continue
            self.menu()
        def updataUser(self):
            global userlist
            name=input("请输入要查找的用户名")
            index = self.mysql.Find_stu(name)
            if index==1:
                print("\t {}已注册".format(name))
                print("请选择操作：")
                print("\t 1.修改用户")
                print("\t 2.删除用户")
                print("\t 3.回到主菜单")
                action=input("请输入对应操作：")
                if action=="1":
                    newName=input("请输入新用户名：")
                    self.mysql.execute(self.mysql.UpdateUserInfo(name,newName))
                elif action=="2":
                    self.mysql.execute(self.mysql.DeleteUser(name))
                self.menu()
            else:
                print("该用户不存在")
                self.menu()
        # def save(self):
        #     global userlist
        #     with open("./data/user.bin","wb+") as f :
        #         dump(userlist,f)
        #         print("\t 已成功保存信息")

        def showAll(self):

            # global userlist
            index=self.mysql.execute(self.mysql.SelectAllUser())
            print("index:",index)
            if len(index)==0:
                print("\t 当前无注册用户")
            else:
                print("当前已注册的用户信息如下：")
                n=1
                for x in index:
                    print("编号：{}\t姓名：{}\t".format(x[0],x[1]))
            self.menu()

    # myfile=open("./data/user.bin","ab+")
    # x=myfile.read()
    # if x==b"":
    #     userlist=list()
    #     print("userlist{}",userlist)
    # else:
    #     myfile.seek(0)
    #     userlist=load(myfile)
    # myfile.close()
except Exception as x :
    with open("./data/log.txt","a",encoding="utf-8") as f:
        f.write("错误时间:{}\n错误信息：{}\n".format(datetime.today(),x))
