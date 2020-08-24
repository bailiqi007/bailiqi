#coding: utf-8
import re
import json
import copy
import traceback


from lib.robot_ext.rf_keyword.rf_logger import logger
from lib.robot_ext.rf_keyword.rf_exception import OK, FAIL, RF_KW_PARAMS_FAIL

__all__ = ["keyword", "OK", "FAIL", "logger"]

"""
def keword(name, tags=(), types=()):
    def decorator(func):
        func.robot_name = name
        func.robot_tags = tags
        func.robot_types = types
        return func
"""
def keword(name=None):
    #logger.trace("enter deco_para")
    def deco_func(func):
        #logger.info(f"enter deco_func {func}")
        def deal_params(params, params_schema):
            """
            参数中文->英文映射，校验，默认值处理
            return expect, new_params
            """
            #中文参数转换为英文
            new_params = {}
            expect = "成功"
            for key, value in params.items():
                if key == "期望结果":
                    expect = value
                    #做个小转换，新关键字采用any 代替 None
                    if expect.upper() == "NONE":
                        expcet = "any"
                    continue
                if "_USECASE_PATH__" in key or "__USECASE_NAME__" in key or "_timeout" in key:
                    continue
                param_schema_list = list(filter(lambda x: x["name"] == key, params_schema))
                if not param_schema_list:
                    raise RF_KW_PARAMS_FAIL(f'参数 name->id 映射出错，可能传入不在定义范围内的参数, 请核对: {key}={value}')

                param_schema = param_schema_list[0]
                en_name = param_schema["id"]
                new_params[en_name] =  value

            return (expect, new_new_params)
            
        def run(*arg, **params):
            pass
            
        logger.info("enter wrapper")
        logger.info("-----wrapper :before func---")
        logger.info(f"{func.__doc__}")

        logger.info(json.dumps("123", ensure_ascii=False, indent=4))

        kw_schema={"name":"新增区域","tags":"未完成"}
        wrapper_func = run
        wrapper_func.__name__ = func.__name__
        wrapper_func.__doc__ = func.__doc__
        wrapper_func.robot_name = kw_schema["name"]
        wrapper_func.robot_tags = kw_schema["tags"]

        return wrapper_func
    return deco_func


