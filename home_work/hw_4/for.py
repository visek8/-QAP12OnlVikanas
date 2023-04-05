# 1 Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно

a = 5
b = 10
s = 0


def fun_1(a, b, s):
    for i in range(a, b + 1):
        s = s + i
    print(s)


fun_1(a, b, s)

# 2 Найти сумму всех натуральных чисел в от A до B
a_1 = int(input('Введите наименьшее число: '))
b_1 = int(input('Введите наибольшее число: '))
s_1 = 0


def fun_2(a_1, b_1, s_1):
    for i in range(a_1, b_1):
        s_1 = s_1 + i
    print(s_1)


fun_2(a_1, b_1, s_1)

# 3 Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.

numbers = [int(i) for i in input('Введите 10 чисел через пробел ').split()]
prod = 1
su = 0
k = 0


def fun_3(numbers, su, prod, k):
    for i in numbers:
        if i > 0:
            prod = prod * i
        if i < 0:
            su = i + su
            k = k + 1
    print(numbers, su, prod, k)


fun_3(numbers, su, prod, k)

# 4 Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17

swimmer = {'Бекиш Александр': 21.07, 'Будник Алексей': 20.34, 'Гребень Анастасия': 22.12, 'Казак Анна': 28.17,
           'Дешук Дмитрий': 24.01, 'Давидович Татьяна': 30}


def swim(swimmer):
    for i in swimmer:
        winner = min(swimmer.values())
        winner_dict = {k: w for k, w in swimmer.items() if w == winner}
    print(winner_dict)


swim(swimmer)

# 5. Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5. Напишите программу, которая будет выводить
# уникальное число

unik = [1, 5, 2, 9, 2, 9, 1]


def un(unik):
    for i in unik:
        resalt = (min(unik, key=unik.count))
    print(resalt)


un(unik)
