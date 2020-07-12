---
title: Ubuntu或Centos安装Remote-ssh
date: 2020-03-08 22:39:32
tags: vscode
categories: 技术
---
# 安装Remote-ssh

WIN10 在[更新](https://support.microsoft.com/zh-cn/help/4028685/windows-10-get-the-update)中添加了内置的 OpenSSH 支持，如果没有特殊要求的话便可以抛弃 **PuTTY** 、**KiTTY** 或 **SSHSecureShellClient** 等工具，使用内置 OpenSSH 客户端进行 SSH 链接，也省的考虑压缩算法不一致的问题了。

## 在windows安装 OpenSSH 客户端

1、在开始图标右键，选择应用和功能，弹出如下设置界面，点击可选功能

![1585146590110](安装Remote-ssh/1585146590110.png)

![1585146639489](安装Remote-ssh/1585146639489.png)

2、选择可选功能，弹出管理可选功能（我这个已经安装好了，没有安装的，点击  **添加功能**）

![1585146684084](安装Remote-ssh/1585146684084.png)



3、在弹出的添加功能中选择 OpenSSH 客户端

![img](https:////upload-images.jianshu.io/upload_images/8942745-59134fb6bcf4d8c4.png?imageMogr2/auto-orient/strip|imageView2/2/w/875/format/webp)

4、安装成功后返回即可看到



![img](https:////upload-images.jianshu.io/upload_images/8942745-3ca9fff8375f0949.png?imageMogr2/auto-orient/strip|imageView2/2/w/875/format/webp)

安装成功

### 验证 OpenSSH 客户端

打开cmd，输入ssh

![1585146882016](安装Remote-ssh/1585146882016.png)

# 在ubuntu安装openssh 服务器 

```shell
sudo apt-get install openssh-server
```

参考： https://blog.csdn.net/qq_36381640/article/details/79062662 

# 在vscode设置Remote ssh的config

![1585147367033](安装Remote-ssh/1585147367033.png)

* 快捷键 Ctrl+Shift+P

![1585147405675](安装Remote-ssh/1585147405675.png)

![1585147427023](安装Remote-ssh/1585147427023.png)

# vscode 使用ssh密钥登录远程Linux 



![1585149308919](安装Remote-ssh/1585149308919.png)



![1585149293959](安装Remote-ssh/1585149293959.png)

该成git的.ssh

![1585149532879](安装Remote-ssh/1585149532879.png)

# 免密登录的Remote-ssh

在Centos或者linux上，执行下面的命令：

```shell
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
```

`id_rsa.pub`是自己本地电脑 生成的`公钥`。

如果在本地安装过git。那就是git的公钥，该公钥存放在C盘的`.ssh`文件夹下面。

如果没有在本地安装过git.建议去看廖旭锋的git安装，查看秘钥的生成命令。

# 在Centos上安装Openssh Server

```
安装
yum install openssh-server -y
开机自启动
systemctl enable sshd.service
开启ssh服务
systemctl start sshd.service

```

 \# 至于自制的公钥数据就放置于用户家目录下的 .ssh/authorized_keys 内 

 https://blog.csdn.net/YlanHds/article/details/80164006?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task 

 https://blog.csdn.net/y_silence_/article/details/80255401?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task 