import logging.handlers

# def log():
logger=logging.getLogger("log")
logger.setLevel(logging.DEBUG)
fh=logging.handlers.TimedRotatingFileHandler(filename="./a.log",when="M",interval=0,backupCount=0,encoding="UTF-8")
ch=logging.StreamHandler()
fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
fomatter=logging.Formatter(fmt)
fh.setFormatter(fomatter)
fh.setLevel(logging.DEBUG)
ch.setFormatter(fomatter)
ch.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)


logging.debug("debug")
logging.info("info")
logging.warning("warning")