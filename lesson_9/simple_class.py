#!/usr/bin/python
# -*- coding: utf-8 -*-

class Dog():
    name = ''
    color = ''
    age = 0
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def call(self):
        print('wang wang')
        print('my name is '+self.name)
        print('my color is '+self.color)
        print('my age is '+str(self.age))

class Cat():
    name = ''
    color = ''
    age = 0
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def call(self):
        print('miao miao')
        print('my name is '+self.name)
        print('my color is '+self.color)
        print('my age is '+str(self.age))

dog1 = Dog('doudou', 'black_white', 2)
dog1.call()

cat1 = Cat('ersha', 'white', 3)
cat1.call()
