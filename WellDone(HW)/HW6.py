
# Урок 6. Повторение списков

# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# NumberA = int(input('введите первое число: '))
# Number = int(input('введите кол-во чисел: '))
# NumberD = int(input('введите разницу чисел: '))
# list_1 = []
#
# for i in range(NumberA, Number, NumberD):
#     list_1.append(i)
#     print(i)
#
# print(list_1)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = sorted([1, 2, 0, 9, 2, 4, 7, 6, 5, 3, 8, 10])
print(list_1)
print('введите диапазон. ')
maxnum = int(input('максимальное значение: '))
minnum = int(input('минимальное значение: '))
indexMin = 0
indexMax = 0
print(list_1)
for i in range(len(list_1)):
    if minnum == list_1[i]:
        indexMin = i
    elif maxnum == list_1[i]:
        indexMax = i
for i in range(indexMin, indexMax+1):
    print(list_1[i])

print(f' {indexMin} - {indexMax} ')
 
