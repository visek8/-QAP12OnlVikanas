# 1 Напишите декоратор, который проверял бы тип параметров
# функции, конвертировал их если надо и складывал:
def typed_1(func):
    def add_two_symbols(a, b):
        if type(a) == type(b) == str:
            func(a, b)
        elif type(a) == int:
            a = str(a)
            func(a, b)
        elif type(b) == int:
            b = str(b)
            func(a, b)
        elif type(b) == type(a) == int:
            b = str(b)
            a = str(a)
            func(a, b)

    return add_two_symbols


@typed_1
def func(a, b):
    print(str(a) + str(b))


def typed_2(func):
    def add_three_symbols(a, b, c):
        func()
        if type(a) != type(b) != type(c):
            print(int(a) + int(b) + int(c))
        elif type(a) == type(b) != type(c):
            print(int(a) + int(b) + int(c))
        elif type(a) != type(b) == type(c):
            print(int(a) + int(b) + int(c))
        else:
            print(a + b + c)

    return add_three_symbols


@typed_2
def func_2():
    print('Результат работы декоратора:')


# 2 На вход подаётся некоторое количество (не больше сотни)
# разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19). Выведите их через пробел в порядке
# лексикографического возрастания названий этих чисел в
# английском языке.Т.е., скажем числа 1, 2, 3 должны быть
# выведены в порядке 1, 3, 2, поскольку слово two в словаре
# встречается позже слова three, а слово three -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two'
# является истинным)

def fantik(funk):
    def wrap():
        funk()
        number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:
            'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12:
                            'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17:
                            'seventeen', 18: 'eighteen', 19: 'nineteen'}
        lis = list()
        a = input()
        a = a.split()
        a_lst = list(a)
        result = [int(item) for item in a_lst]
        for i in result:
            if i in number_names:
                lis.append(number_names[i])
        lis.sort()
        num_fin = []
        for i in lis:
            for key, value in number_names.items():
                if i in value:
                    num_fin.append(key)
        print(num_fin)

    return wrap()


@fantik
def funk_4():
    print('Введите любые числа от 0 до 19 включительно через пробел: ')
