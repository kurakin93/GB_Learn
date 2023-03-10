# Урок 5. Рекурсия и алгоритмы

# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = int(input('число - '))
# b = int(input('степень - '))
# def lvlnumber(num, lvl):
#     if lvl == 0:
#         return 1
#     elif lvl == 1:
#         return num
#     else:
#         num = num * (lvlnumber(num, lvl-1))
#         return num
# print(lvlnumber(a, b))


# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

# a = int(input('число a - '))
# b = int(input('число b - '))
# def sumnumab(a, b):
#     if b == 0:
#         return a
#     else:
#         a = 1 + sumnumab(a, b - 1)
#         return a
#
#
# print(sumnumab(4, 3))
