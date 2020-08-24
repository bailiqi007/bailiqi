import traceback

from toolbox.robot_ext.rf_keyword.rf_logger import logger
from toolbox.robot_ext.rf_keyword.rf_exception import OK, FAIL, RF_KW_FAIL

class Result():
    # factory method to initialize the appropriate result class
    # according to the type of +result+
    @classmethod
    def build(self, result):
        if isinstance(result, OK) or isinstance(result, FAIL):
            #logger.info('关键字执行完毕，结果为期望类型')
            return ResultWithExpectation(result)
        elif isinstance(result, Exception):
            #logger.info('关键字执行完毕，结果为异常类型')
            return ResultWithException(result)
        else:
            logger.info('关键字执行完毕，结果为返回值类型')
            return ResultWithReturn(result)
    
class ResultWithReturn(result):
    def __init__(self, result):
        self.result = result
    def expect(self, exp="any"):
        if exp in ("any", "成功"):
            return True, self.result
    
class  ResultWithExpectation(result):
    def __init__(self, result):
        self.result = result
        self.more_info = ""
        for item in result.args:
            self.more_info += f'{item}'
        self.more_info = self.more_info.strip()
    
    def expect(self, exp="any"):
        actual = str(self.result)
        if exp == "any":
            return True, f'期望对比成功：期望结果 => {exp} 实际结果 => {actual}; {self.more_info}'
        elif actual == exp:
            return True, f'期望对比成功，期望结果 => {exp} 实际结果 => {actual}; {self.more_info}'
        else:
            return False, f'期望对比失败，期望结果 => {exp} 实际结果 => {actual}; {self.more_info}'

class ResultWithException():
    """关键字抛出异常,且不是RF定义的成功与失败异常"""
    def __init__(self, result):
        self.result = result

    def expect(self, exp="any"):
        actual = str(self.result)
        return False, f'期望对比失败,期望结果 => {exp} 实际结果 => 关键字执行过程中抛出异常, {actual}'


