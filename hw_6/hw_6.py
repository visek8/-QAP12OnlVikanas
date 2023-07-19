# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

f_1 = open('text_1.txt', 'w')
f_1.write('5 33 8 77 63')
f_1.close()
f_2 = open('text_1.txt', 'r')
file_info = f_2.read()
print(type(file_info))
str_arr = file_info.split(' ')
print(str_arr)
if len(str_arr) > 3:
    print(str_arr[0])
    print(str_arr[1])
    print(str_arr[-1])
    print(str_arr[-2])
else:
    print('Error')
f_2.close()

# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.
with open("text_1.txt", "r") as n:
    file_2 = n.read()
    arr = file_2.split(' ')
    f_4 = open('text_3.txt', 'w')
    f_3 = open('text_2.txt', 'w')
    for i in arr:
        if int(i) % 2 == 0:
            s = str(i) + ' '
            f_3.write(s)
        else:
            s = str(i) + ' '
            f_4.write(s)
    f_4.close()
    f_3.close()

# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты
with open('text_1.txt') as f:
    number_lines = f.readlines()

with open('text_1.txt', 'w') as f:
    for line in number_lines:
        line = line.split(' ')
        f.write(' '.join(map(lambda x: str(float(x) ** 2), line)))

# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа

with open('binfile_1.bin', 'wb') as b_1:
    num_1 = [5, 10, 15, 20, 25, 30]
    t_1 = bytearray(num_1)
    b_1.write(t_1)
with open('binfile_2.bin', 'wb') as b_2:
    num_2 = [7, 12, 17, 22, 27, 32]
    t_2 = bytearray(num_2)
    b_2.write(t_2)
with open('binfile_1.bin', 'rb') as bb_1:
    bin_1 = bb_1.read()
with open('binfile_2.bin', 'rb') as bb_2:
    bin_2 = bb_2.read()
with open('binfile_1.bin', 'wb') as b_11:
    b_11.write(bin_2)
with open('binfile_2.bin', 'wb') as b_22:
    b_22.write(bin_1)
