import time

from datetime import datetime

from user import User

try:
    name=input("请输入登陆名：")
    pwd=input("请输入登陆密码:")
    x=User(name,pwd)
except Exception as x :
    with open("./data/log.txt","a",encoding="utf-8") as f:
        f.write("错误时间:{}\n错误信息：{}\n".format(datetime.today(),x))
