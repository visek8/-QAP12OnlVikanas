# задание 1.3
print("x = ", 17 / 2 * 3 + 2)

print("x = ", 2 + 17 / 2 * 3)

print("x = ", 19 % 4 + 15 / 2 * 3)

print("x = ", (15 + 6) - 10 * 4)

print("x = ", 17 / 2 % 2 * 3 ** 3)

# задание 1.4
age_1 = 23
age_2 = 78
age_3 = 33
age_s = age_1 + age_2 + age_3
print("Сумма возраста 3-х соседе равна: ", age_s)
age_sa = age_s / 3
print("Средний арифметический возраст равен: ", age_sa)

# 1
a = -1.6
b = 2.99
print(int(a))
print(int(b))

# 2
txt = 'www.my_site.com#about'
print(txt.replace("#", "/"))

# 3
d = "stroka"
c = "ing"
print(d + c)

# 4
s = "Ivanou Ivan"
m = s.split(' ')
s = m[1] + ' ' + m[0]
print(s)

# 5
st = ' Отличный день! '
print(st.strip())

# 6
school = {'1A': 25, '11B': 20, '5Г': 24, '6А': 18, '10Е': 20, '9Б': 26, '9А': 20, '8Г': 17, '7Д': 22, '3А': 15}

# 7
sp = [56, 'sun', 'summer', 'Lana', 'Del', 'Rey']
print(sp[1])

# 8
str_1 = 'employ'
str_2 = 'employment'
print(str_1 in str_2)

# 9
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])

# 10
num = [1, 5, 2, 9, 2, 9, 1]
set_num = set(num)
list_num = list(set_num)
print(list_num)
