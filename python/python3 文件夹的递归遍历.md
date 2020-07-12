---
title: python引用不同文件操作
date: 2020-03-18 21:19:02
tags: python
categories: 技术
---
#  python3 文件夹的递归遍历

* 给出一个文件目录，返回该目录下的所有内容

```python
import os

def dfs(file_name_path ,file_name, depth , max_depth ,my_list) :
   
    if os.path.isdir(file_name_path) == False:
        return 
        
    if depth == max_depth:
        my_list.append(file_name)
        return 

    file_name_list = os.listdir(file_name_path)
    for temp_name in file_name_list:
        dfs(file_name_path + '/' +temp_name ,temp_name, depth + 1 , max_depth,my_list)

my_list = []
dfs("./基础知识" , " ",0 , 2,my_list  )

for i in my_list:
    print(i)
```

