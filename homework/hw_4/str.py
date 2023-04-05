# 1 Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.
def a():
    v: str = 'grfnklgbjksb'
    print(len(v), v[0], v[-1], v[2], v[-3])


a()


# 2 Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку
def s():
    m: str = 'bhdjkbahjkcbaj'
    print(m[0:8])
    pol = len(m) / 2  # узнаем середину списка
    n: float = pol - 2  # узнаем начало среза
    k: float = pol + 2  # узнаем конец среза
    print(n, k, m[5:9], m[2::3], m[::-1])


s()


# 3 Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# ваше имя
def p():
    y: str = 'my name is name'
    print(y.rfind('name'))
    y = y[:11]
    print(y + 'Viktoryia')


p()

# 4  Есть строка: test_tring = "Hello world!", необходимо
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”
test_tring: str = 'Hello world!'


def kp(test_tring):
    test_tring: str
    test_tring = 'Hello world!'
    a = test_tring.find('w')
    b = test_tring.count('l')
    c = test_tring.startswith('Hello')
    d = test_tring.endswith('qwe')
    print(a, b, c, d, sep='\n')


kp(test_tring)
