---
title: python的装饰器使用
date: 2020-03-03 21:19:02
tags: python
categories: 技术
---
# python 3的装饰器使用方法

* 装饰器就是在`一个函数的前后执行一些代码`
* 所需要的知识是 `高级函数`+`函数嵌套`=`装饰器`
* 高级函数是指：`以函数作为参数`
* ​                            `返回值是函数`

* 嵌套函数:`在函数里面定义函数`

* `实用的`嵌套函数,robot frame work的装饰器

  ```python
  def keyword(name=None,tags=(),types=()):
      print("enter keyword 1")
      def decorator(func):
          print("enter decorator 1")
          def wrapper(*args, **kwargs):
              print("enter wrapper 1")
              res = func(*args, **kwargs)
              print("enter wrapper 2")
              return res
          print("enter decorator 2")
          return wrapper
      print("enter keyword 2")
      return decorator
  
  @keyword(name=None,tags=(),types=())
  def f3():
      print("f3")
  #嵌套了3层
  print(f3()) # f3 = keyword(name="zmy",tags=(),types=())(f3)
                 # = deco_func(f3)
                 # = wrapper
       # f3() = wrapper()
   print(f3.__name__)
  #输出结果是：
  nter keyword 1
  enter keyword 2
  enter decorator 1
  enter decorator 2
  enter wrapper 1
  f3
  enter wrapper 2
  None
  #输出结果是:
  wrapper
  ```

  