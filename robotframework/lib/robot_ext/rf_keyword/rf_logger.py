#encoding:utf-8
#适配RF的logger函数，调整debug等级
import time
from robot.api import logger as rf_logger


class logger(object):
    @staticmethod
    def loglevel():
        str_level = "DEBUG"
        level_map = {
            "TRACE":0,
            "DEBUG":1,
            "INFO":2,
            "WARN":3,
            "ERROR":4,
            "FATAL":5
        }
        return level_map.get(str_level, 6) #返回指定键的值，如果键不在字典中返回 default 设置的默认值
    
    @staticmethod
    def error(info):
        rf_logger.trace(info)
        if logger.loglevel() <= 4:
            #打印到控制台
            dtime = time.strftime("%Y/%d/%m %H:%M:%S", time.localtime(time.time()))
            msg = f'[ERROR]: {dtime} {info}'
            rf_logger.console(msg)
    
    @staticmethod
    def debug(info):
        rf_logger.trace(info)
        if logger.loglevel() <= 1:
            dtime = time.strftime("%Y/%d/%m %H:%M:%S", time.localtime(time.time()))
            msg = f'[DEBUG]: {dtime} {info}'
            rf_logger.console(msg)
    
    @staticmethod
    def info(info):
        rf_logger.info(info)
        if logger.loglevel() <= 2:
            dtime = time.strftime("%Y/%d/%m %H:%M:%S", time.localtime(time.time()))
            msg = f'[INFO]: {dtime} {info}'
            rf_logger.console(msg)

if __name__ == "__main__":
    logger.debug("hello wo shi zmy")
    logger.info("info ....")
    logger.error("error ....")