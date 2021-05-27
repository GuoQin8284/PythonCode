import logging.handlers
import os

import time

path = os.path.dirname(__file__)

host = "https://author.osid.org.cn"

def init_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    file = path+os.sep+"log"+os.sep+"{}登录接口测试.log".format(time.strftime("%Y-%m-%d %H_%M_%S"))
    fh = logging.handlers.TimedRotatingFileHandler(filename=file, when="D", interval=1, backupCount=5)

    fmt = "%(asctime)s-%(levelname)s-%(name)s [%(filename)s %(funcName)s-%(lineno)d]:%(message)s"
    formater = logging.Formatter(fmt)

    sh.setFormatter(formater)
    fh.setFormatter(formater)

    logger.addHandler(sh)
    logger.addHandler(fh)



