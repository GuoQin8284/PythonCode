# 每日生成一个日志文件
import logging.handlers

# 创建日志器
import time

logger=logging.getLogger("hehe")

# 创建处理器
sh = logging.handlers.TimedRotatingFileHandler(filename="c.log",when="M",interval=1,backupCount=5,encoding="utf-8")
# tfh = logging.handlers.TimedRotatingFileHandler('time.log', when='s', interval=20, backupCount=1, encoding='utf-8')


# 创建格式器
fmt = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
format=logging.Formatter(fmt)
# 格式化器 放入 处理器
sh.setFormatter(format)

# 处理器 放入 日志器

logger.addHandler(sh)
logger.setLevel(logging.DEBUG)


# 产生日志
while True:
    logger.debug("调试级别")
    logger.info("一般级别")
    logger.warning("警告级别")
    logger.error("错误级别")
    logger.critical("严重错误级别")
    time.sleep(1)