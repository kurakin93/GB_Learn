# a = int(input("input a "))
# b = int(input("input b "))
# c = int(input("input c "))
#
# print(f'a + b = {(a+b)*2}') # Задача 1 периметр прямоугольника
#
# print(f'a + b + c = {a+b+c}') # Задача 2 сумма трех чисел
#
# print(f'a * b = {a*b}') # Задача 3 площадь прямоугольника


# Меньшее число из двух
# a = int(input("input a "))
# b = int(input("input b "))
# if a < b:
#     print(f'B more  than A')
# elif a == b:
#     print(f'they are equal')
# else:
#     print(f'A more  than B')
# Четырехзначное число или нет
# a = input("input number ")
# if 1000 < a < 10000 or -10000 < a < -1000:
#     print(f'Number four-digit')
# else:
#     print(f'Number no four-digit')

# Второй вариант решения задачи
# a = input()
# if '-' in a:
#     if len(a) == 5:
#         print('Yes')
#     else:
#         print('No')
# else:
#     if len(a) == 4:
#         print('Yes')
#     else:
#         print('No')
# Третий вариант решения
# a = input()
# print(len(a) == 4)

# пользователь вводит числа с клавиатуры, найти числа кратны 4

# summa = 0
# while True:
#     a = input()
#     if a == '':
#         break
#     if int(a) % 4 == 0:
#         summa += int(a)
# print(summa)

# Задача №1. Общее обсуждение
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
# a = int(input())
# b = int(input())
# print((a+b-1)/a)


# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input())
# b = int(input())
# c = int(input())
# part = a/2+b/2+c/2
# print(round(a/2+b/2+c/2))
# print(f'{round(a/2+b/2+c/2)}')
# print(a, ' + ', b, ' + ', c, ' = ', round(part))
# print('{} + {} + {} = {}'.format(a, b, c, round(part)))

# Задача №7.  Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

# a = int(input('input number year'))
# print(a % 4 == 0)

# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# Number_wagon = 6
# Number_sit_down = int(input('input wagon number to sit down'))
# Number_ticket = int(input('input wagon number ticket'))
# if 1 < Number_ticket < Number_wagon and 1 < Number_sit_down < Number_wagon:
#     print(f' Вагонов {Number_wagon}, сидит в вагоне {Number_sit_down}, билет вагон номер {Number_ticket}')
# else:
#     print('такого вагона нет')

################################################################################################################################


# 1.	Деление чисел. Тонкости деления.
# 2.	Разные варианты приветствия. Админ и пользователь
# a = input('Input user')
# if a == 'Admin':
#     print(f'Дарова {a}')
# else:
#     print(f'Добро пожаловать {a}')
# 3.	Проверка ввода пароля.
# 4.	Контрольно пропускной пункт. Вес машины.
# 5.	Контрольно пропускной пункт. Вес машины с пороговым значением. +- 50 килограмм
# 6.	Контрольно пропускной пункт. Вес машины с пороговым значением. 5% от 10т
# 7.	Покупка товара с акциями. Если стоимость больше 1000р скидка 20%. Если заказ более чем 700р доставка бесплатно
# 8.	Найти наименьшее из двух чисел
# 9.	Найти наименьшее из трёх чисел
# 10.	По заданному часу вывести время суток
# 11.	Выяснить, что одно число является квадратом другого
# 12.	Вычислить площадь треугольника с тремя заданными сторонами
# 13.	Дано число N. Определить является ли оно кратным числу 4 или 6. Легенда про ремонт и транспортировку материалов
# 14.	Является ли шестизначное число счастливым.

#########################################################################################################################################

# Classwork

# 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# a = int(input())  # факториал
# temp = 1
# count = 1
# while count <= a:
#     temp *= count
#     count += 1
#     print(f'{count-1} = {temp}')


# a = 'hello'
# for e in range(1, -6, -3):
# 	print(e)

# for i in range(1, 10): #таблица умножения
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

# for i in range(5): # 0 1 2 3 4
#     print(f'{i}', end="\t")


# for e in range(0, len(0)): # 0,1,2,3,4
# 	print(e[ind])

# 10. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1
# 0 1 1 2 3 5 8 13 21 34 55...
# a = int(input())
# second_el = 1
# first_el = 0
# count = 3
# temp = second_el + first_el
# while temp < a:
#     first_el = second_el
#     second_el = temp
#     temp = second_el + first_el
#     # print(f'{count} = {temp}')
#     count += 1
# if temp == a:
#     print(count)
# else:
#     print(-1)


# 13. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# max_count = 0
# count = 0
# number_days = int(input())
# for _ in range(number_days):
#     temp = int(input())
#     if temp >= 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#             count = 0
# print(max_count)



# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.




# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
## *Пример:*
## [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# a = input('Введите последовательность чисел: ').split()
# text = input('Введите текст: ')
# text = [1, 2, 3, 5, 1, 5, 3, 10]
#
# # text = text.split()
# text = set(text)
# print(text)
# print(f'В нашем тексте {len(text)} уникальных слова')

"""39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива"""

# import random
# import time
# first_list = [random.randint(1, 100) for _ in range(10 ** 6)]
# second_list = [random.randint(1, 100) for _ in range(10 ** 6)]
#
# start = time.perf_counter()
# for el in first_list:
#     if el not in second_list:
#         print(el)
# end = time.perf_counter()
# print(end - start)
#
# start = time.perf_counter()
# second_list = set(second_list)
# for el in first_list:
#     if el not in second_list:
#         print(el)
# end = time.perf_counter()
# print(end - start)


'''41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
 у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество
 элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.  3 4 2 5 6 3'''

# some_list = [int(input()) for _ in range(int(input('Введите кол-во чисел: ')))]
# count = 0
# for ind in range(1, len(some_list) - 1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         count += 1
# print(count)

'''43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел, пока не введут 0. Все числа списка находятся на разных строках.  2 3 2 4 5 3 3'''
#
# some_list = []
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     some_list.append(number)
#
# count_dict = {}  # 2: 2, 3: 3, 4: 1, 5: 1
#
# for el in some_list:
#     if count_dict.get(el):
#         count_dict[el] += 1
#     else:
#         count_dict[el] = 1
#
# count = 0
# for value in count_dict.values():
#     count += value // 2
# print(count)

# some_dict = {1: 4, 4: 8}
# print(some_dict.get(5, 'Такого ключа нет!'))


"""45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
Программа получает на вход одно натуральное число k, не превосходящее 10 ** 5.
Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
(перестановка чисел новую пару не дает)."""


# def sum_div(n):
#     summa = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             summa += i
#     return summa
#
#
# summ_dict = {}  # 284: 220,
#
# k = int(input())
# for number in range(2, k + 1):
#     if number in summ_dict:
#         if sum_div(number) == summ_dict[number]:
#             print(number, summ_dict[number])
#     summ_dict[sum_div(number)] = number

# Урок 7

# some_list = [1, 2, 3, 4, 5, 6]
# for ind in range(0, len(some_list)):
#     some_list[ind] = str(some_list[ind])
# print(some_list)


# def square(x):
#     return x ** 2
#
#
# new_list = list(map(lambda x: x + 1, some_list))
# print(new_list)

# def even(x):
#     return type(x) == int

# new_list = list(filter(lambda x: type(x) == int, some_list))
# print(new_list)


# some_list = [10, 20, 30, 40]
# some_dict = {}
# print(list(enumerate(some_list)))
# for ind, value in enumerate(some_list):
#     some_dict[ind] = value
#
# print(some_dict)
#
# for ind in range(0, len(some_list)):
#     print(ind, some_list[ind])


# first_list = ('apple', 'orange', 'grape', 'лимон')
# second_list = ['яблоко', 'апельсин', 'виноград']
# print(list(zip(first_list, second_list)))
# for eng, ru in zip(first_list, second_list):
#     print(eng, ru)

# 47. У вас есть код, который вы не можете менять
# (так часто бывает, когда код в глубине программы используется множество раз и
# вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(transormed_values)

# 49. Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой
# далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна



# number = 102 # числа в листе равна этой сумме
# list = [90, 50, 38, 80, 12]
# temp = ()
# # for i in range(len(list)):
# #     for j in range(len(list)):
# #         if list[i] + list[j] == number:
# #             print(f'{i} --- {j} ')
# #             break
#
# for el in list:
#     if number-el in list:
#         print('Yes')
#         break
# else:
#     print('No')
#
#
# import timeimport randomsumma = 102some_list = [random.randint(1, 100000) for _ in range(10 ** 6)]start = time.perf_counter()some_set = set(some_list)for el in some_set:    if summa - el in some_set:        print(el, summa - el)        breakelse:    print('no')end = time.perf_counter()print(end - start)start = time.perf_counter()for el in some_list:    if summa - el in some_list:        print(el, summa - el)        breakelse:    print('no')end = time.perf_counter()print(end - start)
#

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:


# values = [0, 2, 10, 6]
#
# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#     for i in range(len((objects))):
#         if characteristic(objects[i]) == characteristic(objects[0]):
#             return False
#
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
####################################
# list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# new_list = list()
# new1_list = []
# for i in list_1:
#     if i % 2 == 0:
#         new_list.append((i, i**2, i**3))
#
#
# print(new_list)
# print(list(map(lambda x: x*x, new1_list)))
# print(list(zip(new_list, map(lambda x: x*x, new1_list))))
###
# def select(f, col): # вместо нее функцию map
#     return [f(x) for x in col]
#
# def where(f, col): # функцию filtr
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data) # либо select
# print(res)
# res = filter(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res)) # либо select
# print(res)
#################################################

# data = '15 156 89 56 45 12 32 78'
# print(data)
# data = data.split()
# or
# data = '15 156 89 56 45 12 32 78'
# print(data)
# data = list(map(int, data.split()))

# генератор-итератор
# a = [1, 2, 3]
# d = iter(a)
# print(next(d))
# import time
# start = time.perf_counter()
# def f(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr = pr * i
#         yield pr
#
# for i in f(100):
#     print(i)
# 0.00956390000283136 --0.004958199999236967
# end = time.perf_counter()
# print(end - start)
# import time
# start = time.perf_counter()
# pr = 1
# for i in range(1, 101):
#     pr = pr * i
#     print(pr)
# end = time.perf_counter()
# print(end - start)


#шифровка цезаря
# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

# K-M
# O-Q
# E-G
# alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# smeshenie = int(input('Шаг шифровки: '))
# message = input("Сообщение для ДЕшифровки: ").upper()
# itog = ''
# lang = input('Выберите язык RU/EU: ')
# if lang == 'RU':
#     for i in message:
#         mesto = alfavit_RU.find(i)
#         new_mesto = mesto + smeshenie
#         if i in alfavit_RU:
#             itog += alfavit_RU[new_mesto]
#         else:
#             itog += i
# else:
#     for i in message:
#         mesto = alfavit_EU.find(i)
#         new_mesto = mesto + smeshenie
#         if i in alfavit_EU:
#             itog += alfavit_EU[new_mesto]
#         else:
#             itog += i
# print (itog)



# import random
# a = [random.randint(0, 100) for i in range(50)]
# print(a)
# # a = input().split()
# # a = [int(i) for i in a]
# a = [i for i in a if i % 3 == 0]
# print(a)

# Семинар 8



# with open('les8test.txt', 'r', encoding='utf-8') as file:
#     # text = file.read().splitlines()
#     # print(text)
#
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())


# with open('filetest.txt', 'a', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')

import time

# with open('test20.txt', 'r', encoding='utf-8') as file:
#     find_letter = input()
#     count = 0
#     start = time.time()
#     for letter in file.read():
#         if letter == find_letter:
#             count += 1
#     end = time.time()
#     print(count)
#     print(end - start)

# with open('test20.txt', 'r', encoding='utf-8') as file:
#     find_letter = input()
#     start = time.time()
#     print(file.read().count(find_letter))
#     end = time.time()
#     print(end - start)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint
# n = int(input('Введите кол-во элементов в списке: '))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('les8test.txt', 'w', encoding='utf-8') as file:
#     for _ in range(randint(1, n)):
#         file.write(str(randint(0, n - 1)) + '\n')
#
# with open('les8test.txt', 'r', encoding='utf-8') as file:
#     mult = 1
#     for ind in file.read().splitlines():
#         mult *= some_list[int(ind)]
# print(mult)


# with open('file.txt', 'a') as txt:
#     txt.write('Hello!\n')  # разделителей не будет
#     txt.writelines('HEello!')
# dict = {1: 'one', 2: 'two'}
# with open('file1.txt', 'a') as txt:
#     txt.write(dict.int)
    # for item,value in dict:
    #     txt.write(di)



# Создание словаря
d = {'a': 1, 'b': 2, 'c': 3}
t = ( 'abc', 'def', 'ghi', 'jk lmn')
# Бинарные файлы. Запись/чтение кортежа, содержащего строки символов

# 1. Заданный кортеж со строками
T = ( 'abc', 'def', 'ghi', 'jk lmn')

# 2. Запись кортежа T в файл 'myfile5.bin'
# 2.1. Открыть файл для записи
f = open('file.txt', 'wb')

# 2.2. Цикл обхода кортежа
for item in T:
    bt = (item + '\n').encode() # конвертировать (str + '\n') => bytes
    f.write(bt) # записать bt в файл

# 2.3. Закрыть файл
f.close();



