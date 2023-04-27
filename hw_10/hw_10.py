# Цветочница. Определить иерархию и создать несколько цветов.
# Собрать букет с использованием аксессуаров с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов стоимости. Узнать, есть ли цветок в букете.

class Flower:
    def __init__(self, name, coast, date):
        self.name = name
        self.coast = coast
        self.date = date


class Accessory:
    def __init__(self, name, coast):
        self.name = name
        self.coast = coast


sunflower = Flower('Sunflower', 20, 5)
aster = Flower('Aster', 15, 4)
carnation = Flower('Carnation', 10, 3)
cornflower = Flower('Cornflower', 5, 2)
сrepe = Accessory('Crepe', 5)


class Buqet:
    def __init__(self, *i):
        self.buqet = list()
        for i in i:
            self.buqet.append(i)

    def __str__(self):
        str = "Buqet: \n\t"
        for i in self.buqet:
            str += i.name + '\n\t'
        str += f'\nCoast: {self._coast}'
        return str

    def _coast(self):
        coast = 0
        for i in self.buqet:
            coast += i.coast
        return coast

    def withering(self):
        time_f = 0
        flow = 0
        for i in self.buqet:
            if isinstance(i, Flower):
                time_f += i.date
                flow += 1
        res = time_f / flow
        print('The bouquet will begin to fade through: ' + str(res))

    def sort(self):
        flower = list()
        for i in self.buqet:
            if isinstance(i, Flower):
                flower.append(i)
        print('Flowers in buqet: ')
        for i in flower:
            print(" " + i.name)
        return flower.sort(key=lambda x: x.coast)

    def find(self, name):
        for i in self.buqet:
            if i.name == name:
                print(f'Flower: {i.name} (coast - {i.coast}, withering - {i.date})')


buqet = Buqet(sunflower, cornflower, сrepe)
print(buqet)
buqet.find('Cornflower')
buqet.sort()
buqet.withering()
