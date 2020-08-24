# coding:utf-8
# RF框架关键字异常类
# 2020/7/27 周梦园

class RF_Exception(Exception):
    pass

class OK(RF_Exception):
    def __str__(self):
        return "成功"

class FAIL(RF_Exception):
    def __str__(self):
        return "失败"

class RF_KW_FAIL(RF_Exception):
    pass

class RF_KW_PARAMS_FAIL(RF_Exception):
    """获得关键字"""
    pass