# Цветочница.
# Определить иерархию и создать несколько цветов.
# Собрать букет с использованием аксессуаров с
# определением его стоимости.
# Определить время его увядания по среднему времени
# жизни всех цветов в букете.
# Позволить сортировку цветов стоимости
# Узнать, есть ли цветок в букете.

class Flower:
    def __init__(self, colour, cost, date):
        self.colour = colour
        self.cost = cost
        self.date = date



class Sunflower(Flower):
    pass


class lavender(Flower):
    pass


class Aster(Flower):
    pass
class Buket:
    pass

sun = Sunflower('red', 2, 3)
print(sun)
