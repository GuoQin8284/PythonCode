import logging.handlers

def log():
    logger=logging.getLogger("log")
    logger.setLevel(logging.DEBUG)

    fh=logging.handlers.TimedRotatingFileHandler(filename="./a.log",when="M",interval=0,backupCount=0,encoding="UTF-8")
    ch=logging.StreamHandler()
    fmt="%(asctime)s %(levelname)s %(name)$ %(funcName)s %(lineno)d"
    fomatter=logging.Formatter(fmt=fmt)
    fh.setFormatter(fomatter)
    fh.setLevel(logging.DEBUG)
    ch.setFormatter(fomatter)
    ch.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.addHandler(ch)