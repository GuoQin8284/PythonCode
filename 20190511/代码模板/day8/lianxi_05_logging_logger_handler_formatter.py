# 将日志信息同时输出到控制台和文件中


# 创建日志器
import logging

logger=logging.getLogger("value")
# 设置日志输出级别
logger.setLevel(logging.DEBUG)

# 创建处理器--终端处理器对象
sh=logging.StreamHandler()
# 创建处理器--文件处理器对象
fh=logging.FileHandler("b.log",encoding="utf-8")


# 创建格式器
fmt = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
formatter=logging.Formatter(fmt)
# 把格式器 放入 处理器
sh.setFormatter(formatter)
fh.setFormatter(formatter)

# 处理器 放入 日志器
logger.addHandler(sh)
logger.addHandler(fh)

# 产生日志
# 打印五个级别的日志
logger.debug("调试级别")
logger.info("一般级别")
logger.warning("警告级别")
logger.error("错误级别")
logger.critical("严重错误级别")