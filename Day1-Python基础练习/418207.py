#!/usr/bin/env python
# coding: utf-8

# ### 作业一：输出 9*9 乘法口诀表(注意格式)
# 
# 注意：提交作业时要有代码执行输出结果。

# In[1]:


def table():
    #在这里写下您的乘法口诀表代码吧！
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{}*{}={}'.format(j, i, j * i), end='\t')
        print('')


if __name__ == '__main__':
    table()


# ### 作业二：查找特定名称文件
# 遍历”Day1-homework”目录下文件；
# 
# 找到文件名包含“2020”的文件；
# 
# 将文件名保存到数组result中；
# 
# 按照序号、文件名分行打印输出。
# 
# 注意：提交作业时要有代码执行输出结果。

# In[2]:


#导入OS模块
import os
#待搜索的目录路径
path = "Day1-homework"
#待搜索的名称
filename = "2020"
#定义保存结果的数组
result = []

def findfiles():
    #在这里写下您的查找文件代码吧！
    for root, dirs, files in os.walk(path):
        for name in files:
            if(filename in name):
                result.append(name)
    for i in range(len(result)):
        print(str(i+1)+'\t'+result[i])

if __name__ == '__main__':
    findfiles()

