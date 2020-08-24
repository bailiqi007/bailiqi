# encoding=utf-8
import logging,time


# log_path是存放日志的路径
import os
'''
cur_path = os.path.dirname(os.path.realpath(__file__))
#print(cur_path)
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)
class Log(object):

    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式 [%(asctime)s] [%(pathname)s
        self.formatter = logging.Formatter('[%(asctime)s][%(filename)s  -> %(lineno)d] - %(levelname)s : %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, *message):
        self.__console('debug', message)

    def info(self, *message):
        self.__console('info', message)

    def warning(self, *message):
        self.__console('warning', message)

    def error(self, *message):
        self.__console('error', message)


log = Log()
'''



#coding:utf-8
import logging

'''
import logger
mylog = logger.TestLog(__file__).getlog()

'''

cur_path = os.path.dirname(os.path.realpath(__file__))
##print("cur   ",cur_path)
log_path = os.path.join(os.path.realpath(cur_path), 'logs/')
#print(log_path)
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)
class TestLog(object):
    '''
封装后的logging
    '''
    def __init__(self , logger = None):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        self.log_path = log_path
        self.log_name = self.log_path + self.log_time + 'test.log'
 
        #fh = logging.FileHandler(self.log_name, 'w+')  # 追加模式  这个是python2的
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.INFO)
        #fh.setLevel(logging.DEBUG)
 
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        #ch.setLevel(logging.ERROR)
 
        # 定义handler的输出格式 
        formatter = logging.Formatter('[%(asctime)s] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] %(message)s' )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
 
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
 
        #  添加下面一句，在记录日志之后移除句柄
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()
 
    def getlog(self):
        return self.logger



def test():
    log = TestLog().getlog()
    a = "asdasd"
    log.info("愤怒的小猥琐");
    log.info("愤怒的小猥琐");

def test2():
    log = TestLog().getlog()
    a = "asdasd"
    log.info("222222");
    log.info("222222");

if __name__ == "__main__":
    test()
    test2()
 
     