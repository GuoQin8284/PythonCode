from datetime import datetime

from user.user1 import User1
import logging

try:
    x=User1("root","root")
    logging.debug("登录信息:root,root")

except Exception as x :
    with open("../data/log.txt","a",encoding="utf-8") as f:
        f.write("错误时间:{}\n错误信息：{}\n".format(datetime.today(),x))
        logging.debug("错误时间:{}\n错误信息：{}\n".format(datetime.today(),x))
