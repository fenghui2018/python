#!/usr/bin/python
# -*- coding: utf-8 -*-

class Animal(object):
    name = ''
    color = ''
    age = 0

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def call(self):
        print('my name is '+self.name)
        print('my color is '+self.color)
        print('my age is '+str(self.age))

class Dog(Animal):
    def __init__(self, name, color, age):
        super(Dog, self).__init__(name, color, age)
    def call(self):
        print('wang wang')
        super(Dog, self).call()

class Cat(Animal):
    def __init__(self, name, color, age):
        super(Cat, self).__init__(name, color, age)

    def call(self):
        print('miao miao')
        super(Cat, self).call()

dog1 = Dog('doudou', 'black_white', 2)
dog1.call()

cat1 = Cat('ersha', 'white', 3)
cat1.call()
