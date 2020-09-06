#coding:utf-8
"""
一个单元测试的例子
"""

def testit(func, *nkwargs, **kwargs):
    """
    作用：提供了一个执行测试的环境，对有疑问的地方调用，调用函数。
    函数如果执行成功，则返回True和函数的返回值；
    函数如果执行失败，则返回False和函数的报错原因
    """
    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception as diag:
        result = (False, str(diag))
    return result

def test():
    funcs = (int, float)
    vals = (1234, 12.34, "1234", "12.34")

    for eachFunc in funcs:
        print("_" * 20)
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print(f"{eachFunc.__name__}({eachVal}) = {retval[1]}")
            else:
                print(f"failed {eachFunc.__name__}({eachVal}) = {retval[1]}")

if __name__ == "__main__":
    test()