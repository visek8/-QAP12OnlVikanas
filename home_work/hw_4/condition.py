# 1 Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число
a = 89


def func_1(a):
    if a > 0:
        a = a + 1
    return a


func_1(a)

# 2  Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.

b = int(input())
c = int(input())
d = int(input())
k = 0


def func_2(b, c, d, k):
    if b > 0:
        k = k + 1
    if c > 0:
        k = k + 1
    if d > 0:
        k = k + 1
    return k


func_2(b, c, d, k)

# 3 Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются)

year = int(input())


def func_3(year):
    if year % 4 != 0:
        print('365')
    elif year % 100 != 0:
        print('366')
    elif year % 400 != 0:
        print('365')
    else:
        print('366')


func_3(year)

# 4 Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).

day = int(input())


def func_4(day):
    if day == 1:
        print('Понедельник')
    elif day == 2:
        print('Вторник')
    elif day == 3:
        print('Среда')
    elif day == 4:
        print('Четверг')
    elif day == 5:
        print('Пятница')
    elif day == 6:
        print('Суббота')
    elif day == 7:
        print('Воскресенье')


func_4(day)

# 5 Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер едини- цы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах.

m = int(input('Введите число от 1 до 5: '))
n = int(input('Введите массу: '))


def func_5(m, n):
    if m == 1:
        print(n, 'килограмм')
    elif m == 2:
        n = n / 1000000
        print(n, 'килограмм')
    elif m == 3:
        n = n / 1000
        print(n, 'килограмм')
    elif m == 4:
        n = n * 1000
        print(n, 'килограмм')
    elif m == 5:
        n = n * 100
        print(n, 'килограмм')


func_5(m, n)
