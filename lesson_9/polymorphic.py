class Animal(object):
    def call(self):
        print('call')

class Dog(Animal):
    def call(self):
        print('wang wang')

class Cat(Animal):
    def call(self):
        print('miao miao')

def f(animal):
    animal.call()


dog = Dog()
cat = Cat()

f(dog)
f(cat)

"""
class Dog(object):
    def call(self):
        print('wang wang')

class Cat(object):
    def call(self):
        print('miao miao')

def f(animal):
    animal.call()


dog = Dog()
cat = Cat()

f(dog)
f(cat)
"""
