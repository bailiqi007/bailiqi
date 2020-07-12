---
title: python引用不同文件操作
date: 2020-03-18 21:19:02
tags: python
categories: 技术
---
# python3 json的递归遍历

* 给出一个json的key值，返回对应的value
* 学习递归的视频https://www.bilibili.com/video/av43466895/?spm_id_from=333.788.videocard.0

```python
#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data1 = {
    "ping":{
        "status":{
            "satatus": "xxxxx",
            "addrList1": "vvvvvv",
            "addrList2": "zzzzzz"
        }
    }

}
 
def dfs(key_name,data,depth,my_list):
    print("!!!!!!!!!tag   " ,key_name ,data)

    if type(data).__name__ != 'dict':
        return
   
    for key in data:
        if key == my_list[depth] :
            dfs(key,data[key],depth+1,my_list)

json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("sa asasas!!!!!!!!!!!!!    ",data2)
for i in data2:
    print("####### " , i)
my_list = ["ping" , "status" , "satatus"] 
dfs("NULL" ,data2 , 0 , my_list)
```

# 第2版

```python
#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data1 = {
    "ping":{
        "status":{
            "satatus": "xxxxx",
            "addrList1": "vvvvvv",
            "addrList2": "zzzzzz"
        }
    }

}
 
def dfs(key_name,data,depth,my_list):
    if len(my_list) == depth:
        return data
    if type(data).__name__ != 'dict':
        return
    for key in data:
        if key == my_list[depth] :
           return dfs(key,data[key],depth+1,my_list)


json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("sa asasas!!!!!!!!!!!!!    ",data2)
for i in data2:
    print("####### " , i)
my_list = ["ping" , "status" ,"asdasd"] 

ss = dfs("NULL" ,data2 , 0 , my_list)
print("asdasd   " , ss)
```

# 第3版

```python
#!/usr/bin/python3
 
import json
 
# Python 字典类型转换为 JSON 对象
data1 = {
    "ping":{
        "status":{
            "satatus": "xxxxx",
            "addrList1": "vvvvvv",
            "addrList2": "zzzzzz"
        }
    }

}
 
def dfs(key_name,data,depth,my_list):
    if len(my_list) == depth:
        return data
    if type(data).__name__ != 'dict':
        return
    for key in data:
        if key == my_list[depth] :
           return dfs(key,data[key],depth+1,my_list)


json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("sa asasas!!!!!!!!!!!!!    ",data2)
for i in data2:
    print("####### " , i)
my_list = ["ping" , "status" ,"asdasd"] 

ss = dfs("NULL" ,data2 , 0 , my_list)
print("asdasd   " , ss)
```

