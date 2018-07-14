1970学院出品

### 赋值语句
赋值语句的作用: 将对象赋给一个名称。

* 赋值语句建立对象引用值
* 变量名在首次赋值时被创建
* 变量在引用前必须先赋值
* 执行隐式赋值的一些操作

```
# 隐式赋值
模块导入
函数和类的定义
for循环变量以及函数参数
```

变量名的命名规则:

语法: (下划线或字母)+(任意数目的字母、数字或下划线)

* 区分大小写
* 禁止使用保留字

### 分支语句

分支语句用来选择某些语句执行。

```
if <test1>:
    <statements1>
elif <test2>:
    <statements2>
else:
    <statements3>
```

### 循环语句

循环语句主要用来执行不断重复的语句。

```
while <test>:
    <statements1>
else:
    <statements2>
```


```
for <target> in <object>:
    <statements>
else:
    <statements>
```


几个重要的语句:

* break 跳出最近所在的循环
* continue 调到最近所在循环的开头处
* pass 什么事情也不做，只是空占位语句
* else 只有当循环正常离开时才会执行(即没有碰到break语句)