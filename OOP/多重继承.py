class Animal(object):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixIn(object):
    def eat(self):
        print('They all eat meat')

class HerbivoresMixIn(object):
    def eat(self):
        print('They all eat grass')

'''多重继承， 一个子类就可以继承多个父类的功能'''
#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#各种动物
class Dog(Mammal, RunnableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

s = Dog()
s.run()

