#!/usr/bin/python
# -*- coding: utf-8 -*-

def add(x, y):
    return x+y

print(add(1, 2))
print(add('hello', 'world'))


# 画内存模型
def f(s):
    s = 'xxx'

s = 'yyy'
print s
f(s)
print s

def f1(l):
    l.append('xxx')

l = [1, 2]
print l
f1(l)
print l

# 参数匹配
def f(book):
    print book

#f()
f('python')

# 默认参数
def f(book='python'):
    print book

f()
f('c')

def f(*books):
    print books

f('c', 'python', 'go')

l = ['c', 'python', 'go']
f(*l)

def f(**books):
    print books

f(c='c', p='python', g='go')

languages = {
    'c': 'c',
    'p': 'python',
    'g': 'go'
}
f(**languages)

def f(a, b, c):
    print a, b, c

# 非关键字参数
f(1, 2, 3)
# 关键字参数
f(c=3, b=2, a=1)

def f(a, b='b', c='c'):
    print a, b, c

f(1)
f(1, b=2)
#f(c=3, 1)
f(c=3, a=1)

# special
#def f(a, b='xxx', c):
#    print a, b, c
#def f(*books, a='xxx'):
#    print books, a
