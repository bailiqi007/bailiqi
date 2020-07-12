---
title: python引用不同文件操作
date: 2020-03-02 21:19:02
tags: python
categories: 技术
---
* 众所周知，如果.py文件不在当前路径，那么就不能import。而包的引用是在`python编译器`的环境变量的`scripts`文件夹下面，准确的是在`site-packages`文件夹里面。因此，本文介绍如下两种有效的方法：

# 关键找到python编译器的scripts和在该文件下面新建.pth文件

* 方法1

  修改环境变量，在~/.bashrc里面进行修改，然后source ~/.bashrc

* 方法2

  引入.pth文件

  在site-packages添加一个路径文件，如mypkpath.pth，必须以.pth为后缀，写上你要加入的模块文件所在的目录名称就是了。

* 具体操作，分为两种，windows和linux，先说windows:

  代码如下：

  ```python
  #code/temp/hello.py
  #hello.py
  def hello_test():
      print("执行hello程序")
  #code/test/test.py
  #test.py
  from code.temp.hello import hello_test
  def test():
      print("开始了")
      hello_test()
      print("结束了")
  if __name__ == "__main__":
      test()
  ```

  

* 具体操作如下：

  ```python
  1.找到C:\Users\Sangfor\AppData\Local\Programs\Python\Python36\Lib\site-packages
  2.在site-packages文件夹下面新建一个`mypath.pth`文件
  3.在 mypath.pth文件中写入被导入文件的位置，即在自己电脑上的绝对路径D:\work_007\workspace0\8040\code。
      如上一个例子而言 ，被引用.py文件的绝对位置是D:\work_007\workspace0\8040\code\temp，因此在
  4.写好后保存即可。
  5.在vscode的终端上，进入code/test文件下，输入执行python test(),即可执行
  
  ```

* Linux(ubuntu)的操作

  ```
  1./usr/local/lib/python2.7/dist-packages  （note by shanql， 我是放在这个目录下有效的，所添加的目录一定要存在，不存在则会不成功）
  
    例如：在 /usr/local/lib/python2.7/dist-packages  目录下，创建一个mypython.pth,然后里面写上路径
  
  2./home/xuy/faster_RCNN/py-faster-rcnn/lib，这就解决了lib文件夹下找不到其他文件夹下的py文件的问题了
  ```

  