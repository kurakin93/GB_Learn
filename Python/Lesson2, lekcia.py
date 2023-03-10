#with open('file.txt', 'a') as data:
    # data.write('\n closed 1234 \n')
    # data.write('\n closed 1234 \n')
#######
# with open('file.txt', 'r') as data:
# # path = 'file.txt'
# # data =open('file.txt', 'r')
#     for line in data:
#         print(line)
# data.close()
# exit()


# colors = ['red', 'green', 'blue3']
# data = open('file.txt', 'a')
# data.writelines(colors) # запись значений колор, разделителей не будет
# data.write('\n closed 1234 \n')
# data.close() # обязательно надо его закрыть
#################
######function
# import main as h1
# print(h1.f(2.3))

# def conca(*params):
#     res: str = ""
#     res = 0 ### для цифр
#     for item in params:
#         res += item
#     return res
#
# print(conca('a', 's', 'b'))
# print(conca('1', '2', 'c', '22'))
# print(conca(1, 2, 3)) # ошибка
###
#рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)
#
# for j in range(len(list)):
#     print(list[j])
###
# list = []
# a = ('red', 'blue', 'green')
# list: list = a
# list[0] = 'abs'
# print(type(list)) # class <'tuple'>
# print(list[0])
# t = ('red', 'green', 'blue')
# red, green, blue = t
# list_1 = list(t)
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue
# print(f'{t} - {type(t)}')
# print(f'{list_1} - {type(list_1)}')
# list_1[0] = 'abs'
# print(f'{list_1} - {type(list_1)}')
# print(red)
#####
#словарь

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['up']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

###
#множества
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# a = set(list)
# print(len(a))

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# list_numbers = [1, 2, 3, 4, 5]
# k = int(input("Введите N"))
# list_result = list()
# for i in range(k): # цикл выполнится k
#     list_result.append(list_numbers[len(list_numbers) - 1 - i])
#     print(list_result)
# print()
# for i in range(k-1):
#     list_result.append(list_numbers[i])
#     print(list_result)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dictionary_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# dictionary_2 = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": "S005", "V": "S009", "VIII": "S007"}
# dictionary_3 = {"1": "S001", "2": "S003", "3": "S004", "4": "S005", "5": "S006", "6": "S009", "7": "S007"}
# list_1 = set(dictionary_3)
# print(type(list_1))


# set_1 = set()
# for i in dictionary_1:
#     print(i)
#     for j in i:
#         print(j)
#         set_1.add(i[j])
# print(set_1)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером). list_1 = [0, -1, 5, 2, 3]

# array = [0, -1, 5, 2, 3]
# n = 0
# for i in range(0, len(array)):
#     if array[i] > array[i-1]:
#         n += 1
# print(n)