import logging.handlers

logger=logging.getLogger("ha")

sh = logging.handlers.TimedRotatingFileHandler("./l.log",when="M",interval=2,backupCount=1,encoding="utf-8")

fmt = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
forma = logging.Formatter(fmt)

sh.setFormatter(forma)

logger.addHandler(sh)

logger.setLevel(logging.DEBUG)

logger.debug("debug")

logger.info("info")

logger.warning("warning")

logger.error("error")

logger.critical("critical")

