# 1 Создать lambda функцию, которая принимает на вход
# имя и выводит его в формате “Hello, {name}”
def gen_1():
    name = lambda x: 'Hello, ' + x
    print(name(input('Введите имя: ')))


# 2 Создать lambda функцию, которая принимает на вход
# список имен и выводит их в формате “Hello, {name}” в
# другой список
def gen_2():
    n = (input('Введите список имен через пробел: '))
    n_1 = n.split()
    names_list = list(map(lambda x: 'Hello, ' + x, n_1))
    print(names_list)


# 3 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными
# числами с обработкой исключений
def gen_3():
    try:
        numbers = [34.6, -203.4, 44.9, 68.3, 0, -12.2, 44.6, 12.7]
        num = [i for i in numbers if i > 0]
        print(num)
    except:
        print('Пустое значение')


# 4 Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений
def gen_4():
    try:
        sentence = "thequick brown fox jumps over the lazy dog"
        sent = sentence.split()
        sen = [len(i) for i in sent if i != "the"]
        print(sen)
    except:
        print('Выявлено исключение')


# 5 Напишите две функции - encode и decode принимающие как параметр
# строку и число - сдвиг. (шифр цезаря)


lst_user = input('Введите строку для шифровки: ')
step = int(input('Введите шаг для шифровки: '))


def encode(lst_user, step):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    encode = ''
    for i in lst_user:
        place = alphabet.find(i)
        new_place = place + step
        if i in alphabet:
            encode += alphabet[new_place]
        else:
            encode += i
    print(encode)


message = input('Введите строку для дешифровки: ')
step_1 = int(input('Введите шаг для шифровки: '))

encode(lst_user, step)
