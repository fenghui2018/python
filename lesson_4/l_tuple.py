#!/usr/bin/python
# -*- coding: utf-8 -*-

t = ()
print(type(t))
t1, t2 = (1,), (1)
print(type(t1), type(t2))
t = (1, 'python', 0.1)
print(t)
t = 1, 'python', 0.1
print(t)
t = ('abc', ('def',))
print(t)
t = tuple('python')

# 索引 分片 长度
t = (1, 2, 3, 4)
print(t[0])
print(t[1:3])
print(len(t))

# 合并 重复
t1, t2 = (1, 2), (3, 4)
t3 = t1+t2
print(t3)
print(t3*3)

# 迭代 成员关系
t = (1, 2, 3, 4)
for item in t:
    print item

# 列表推导式
print [x*2 for x in t]

# 方法的使用
print t.index(2)
print t.count(2)


# 不可变性
t = (1, 2, 3, 4)
print t[0]
#t[0] = 111


# 与列表互相转换 画一下内存模型
t = (1, 2, 3, 4)
l = list(t)
l[0] = 111
t = tuple(l)
print t
