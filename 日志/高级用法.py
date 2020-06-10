# import logging
#
# logger = logging.getLogger(name="mylogger")
# logger.setLevel(logging.DEBUG)
#
#
# sh = logging.StreamHandler()
# # sh.setLevel(logging.DEBUG)
#
# fh = logging.FileHandler(filename="./高级用法的log.log", encoding="UTF-8")
# # fh.setLevel(logging.DEBUG)
#
# fmt = "%(asctime)s_%(levelname)s_%(name)s_%(funcName)s_%(lineno)d"
# fm = logging.Formatter(fmt=fmt)
#
# sh.setFormatter(fm)
# fh.setFormatter(fm)
#
# logger.addHandler(sh)
# logger.addHandler(fh)
#
# logger.debug("这是debug")
# logger.info("这是info")
# logger.warning("这是warning")
# logger.error("这是error")
# logger.critical("这是critical")

import time
print(time.strftime("%Y-%m-%d %H:%M:%S"))