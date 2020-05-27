# 导入日志工具
import logging



# 在日志打印之前,设置日志的格式
# logging.basicConfig(level=logging.DEBUG)
fmt = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
'%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcname)s:%(lineno)d)] - %(message)s'
"%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"

logging.basicConfig(level=logging.INFO,filename="./f.log",format="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

# logging.basicConfig(format=fmt)
# 打印五个级别的日志
logging.debug("调试级别")
logging.info("一般级别")
logging.warning("警告级别")
logging.error("错误级别")
logging.critical("严重错误级别")