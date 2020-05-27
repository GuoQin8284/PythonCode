import logging
fmt="%(levelname)s %(filename)s %(funcName)s :%(lineno)d %(thread)d %(asctime)s"
logging.basicConfig(level=logging.DEBUG,filename="log.log",format=fmt)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")