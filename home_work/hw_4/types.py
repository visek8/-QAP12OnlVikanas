# 1 Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

rob = "Robin Singh"
fav = "I love arrays they are my favorite"


def robin(rob):
    rob = list(rob)
    return rob


robin(rob)
robin(fav)

# 2 Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

a = ['Ivan', 'Ivanou']
b = 'Minsk'
c = 'Belarus'


def welcome(a, b, c):
    a = " ".join(a)
    print("Привет, {0}! Добро пожаловать в {1} {2}".format(a, b, c))


welcome(a, b, c)


# 3 Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"

def faw(fav):
    fav = "".join(fav)
    return fav


faw(fav)

# 4 Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

ex = ['cake', '20', 'ball', 'pill', 'love', 'like', '88', 'eight', ' apple', '8']


def ex_4(ex):
    ex.pop(6)
    ex[2] = 'doll'
    return ex


ex_4(ex)
