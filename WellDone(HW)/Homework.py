# # Задача 2: Найдите сумму цифр трехзначного числа.
# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0)

# a = input()
# print(f'Число - {a} Сумма чисел = {int(a[0]) + int(a[1]) + int(a[2])}')



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


# a = int(input('Введите общее колличество журавликов = '))
# temp = a // 6
# if a % 6 == 0:
#     print(f'Петя - {temp}, Сережа - {temp}, Катя - {4*temp}.')
# else:
#     print('Не такое число журавликов!')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no


# a = input('Input number ticket')
# if len(a) == 6:
#     temp = int(a[-1]) + int(a[-2]) + int(a[-3])
#     temp1 = int(a[0]) + int(a[1]) + int(a[2])
#     if temp == temp1:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print('No six number')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes

# 3 2 1 -> no

# n = int(input('размер шоколадки n = '))
# m = int(input('размер шоколадки m = '))
# k = int(input('сколько долек хотите k = '))
# size = n * m
# if size >= k:
#     if k % n == 0 or k % m == 0:
#         print('yes')
#     else:
#         print('no')
# else:
#     print('нету столько долек')
