# Придумать класс и методы к нему, использовать инкапсуляцию, полиморфизм и наследование
class Animal:
    def legs(self, legs):
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

    def voice(self):
        print('Dog say: woof woof woof woof')

    def safe(self, i):
        family = ['mom', 'dad', 'me']
        for i in family:
            if i in family:
                print('hi!')
            else:
                print('go away!')


class Cat(Animal):
    def voice(self):
        print('Cat say: meow meow meow meow meow')

    def hunt(self, i):
        prey = ['mouse', 'shrewmouse', 'rat', 'mole']
        for i in prey:
            if i in prey:
                print('gotcha!')
            else:
                print('I hope you are not a pest')


# animal = Animal(2)
# animal.tail(1)
# animal.ears(3)
dog = Dog()
cat = Cat()
