# 1
def a():
    return v


v: str = 'grfnklgbjksb'
print(len(v), v[0], v[-1], v[2], v[-3])


# 2
def s():
    return m


m: str = 'bhdjkbahjkcbaj'
print(m[0:8])
pol = len(m) / 2  # узнаем середину списка
n: float = pol - 2  # узнаем начало среза
k: float = pol + 2  # узнаем конец среза
print(n, k)  # выводим значения, которые необходимо будет ввести в срез
print(m[5:9])  # выводим 4 символа из середины строки
print(m[2::3])  # выводит элементы с индексами, кратными 3
print(m[::-1])  # перевернули строку


# 3
def p():
    return y


y: str = 'my name is name'
print(y.rfind('name'))
y = y[:11]
print(y + 'Viktoryia')


# 4
def kp():
    return test_tring


test_tring: str = 'Hello world!'
print(test_tring.find('w'))
print(test_tring.count('l'))
print(test_tring.startswith('Hello'))
print(test_tring.endswith('qwe'))
