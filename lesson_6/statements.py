#!/usr/bin/python
# -*- coding: utf-8 -*-

# 赋值语句建立对象引用值
# 变量名在首次赋值时被创建
languages = {
    'c': 'c',
    'p': 'python',
    'g': 'go'
}

print languages
#print t


# 赋值的形式
# 普通赋值
a = 'a'
# 序列赋值
a, b, c = 'a', 'b', 'c'
a, b, c, d, e = 'hello'
print a, b, c, d, e
a = b = 'hello'
print a, b
# 增强赋值
a = 1
a += 1
print a


language = 'python'
if language == 'python':
    print('it is python')
else:
    print('it is other language')


language = 'python'
if language == 'python':
    print('it is python')
elif language == 'c':
    print('it is c')
else:
    print('it is other language')

index = 1

while index < 10:
    print index
    index += 1
else:
    print('finished')

# break
index = 1
while index < 10:
    if index == 5:
        break
    print index
    index += 1
else:
    print('finished')

# continue
index = 1
while index < 10:
    index += 1
    if index > 5:
        continue
    print index
else:
    print('finished')

# pass
#while True: pass


# for
l = ['a', 'b', 'c', 'd']
for i in l:
    print i

for i in range(3):
    print i
