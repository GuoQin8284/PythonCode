import logging.handlers

def log_config():
    logger=logging.getLogger()

    logger.setLevel(logging.INFO)

    sh=logging.StreamHandler()
    fh=logging.handlers.TimedRotatingFileHandler("./log/a.log",when="D",interval=1,backupCount=0,encoding="UTF-8")

    fmt = logging.Formatter("%(asctime)s  %(levelname)s  [%(name)%]  [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    sh.setFormatter(fmt)
    fh.setFormatter(fh)

    logger.addHandler(sh)
    logger.addHandler(fh)