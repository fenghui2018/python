#!/usr/bin/python
# -*- coding: utf-8 -*-

def getup(name):
    print(name+' is getting up')

def eat(name):
    print(name+' eats something')

def go_to_school(name):
    print(name+' goes to school')

def op():
    person1 = 'xiaoming'
    getup(person1)
    eat(person1)
    go_to_school(person1)
    person2 = 'xiaohong'
    getup(person2)
    eat(person2)
    go_to_school(person2)

class Person:
    name = ''
    def __init__(self, name):
        self.name = name

    def getup(self):
        print(self.name+' is getting up')
    
    def eat(self):
        print(self.name+' eats something')

    def go_to_school(self):
        print(self.name+' goes to school')


def oo():
    person1 = Person('xiaoming')
    person1.getup()
    person1.eat()
    person1.go_to_school()

    person2 = Person('xiaohong')
    person2.getup()
    person2.eat()
    person2.go_to_school()

if __name__ == "__main__":
    op()
    oo()
