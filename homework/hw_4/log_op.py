# 1  Присвойте двум переменным любые числовые значения.
a = 46
b = 88


# 2 Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.
def logic_2(a, b):
    print(a < b and b > a)
    print(a > 0 and b == 88)
    print(a == b and b > 2)
    print(45 > a and 0 < b)


logic_2(a, b)


# 3 Аналогично выполните п. 2, но уже используя оператор or.
def logic_3(a, b):
    print(b == 777 or a > 0)
    print(8 < 0 or b > a)
    print(b != 88 or a > 100 or 0 == -1)
    print(a == b or 0 > 888)


logic_3(a, b)

# 4 Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа

c = 'Viktoryia'
d = 'Belarus'


def logic_4(c, d):
    print(len(c) > len(d) or len(d) == 85)
    print(len(c) - len(d) == 2 and len(c) > 0)
    print(len(c) < len(d) and len(c) / 2 < 10)
    print(a == d or d == '')


logic_4(c, d)
