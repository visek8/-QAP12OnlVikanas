# Придумать класс и методы к нему, использовать инкапсуляцию, полиморфизм и наследование
class Animal:
    def __init__(self, legs):
        self.legs = legs
        print('I have', self.legs, 'legs')

    def tail(self, tail):
        self._tail = tail
        print('I have ', self._tail, ' tail')

    def ears(self, ear):
        self.__ear = ear
        print('I have ', self.__ear, ' ears')


class Dog(Animal):
    nutrition = 'predator'

    def __init__(self):
        print('Dog say: woof woof woof woof')
class Cat(Animal):
    def __init__(self):
        print('Cat say: meow meow meow meow meow')




# animal = Animal(2)
# animal.tail(1)
# animal.ears(3)
dog = Dog()
cat = Cat()
