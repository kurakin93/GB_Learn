# Урок 7. Функции высшего порядка

# Задача 34:
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод:
# Парам пам-пам

data_word = (input('Введите фразу: ')).split()
vowel_letters_rus = 'йуеаоэяиюы'


def count_vowel_letters(data):
    count_list = []
    count = 0
    for word in data:
        for letters in word:
            for letters_rus in vowel_letters_rus:
                if letters == letters_rus:
                    count += 1
        count_list.append(count)
        count = 0

    if count_list.count(next(iter(count_list))) == len(count_list):
        print('Парам пам-пам')
    else:
        print('Пам парам')

count_vowel_letters(data_word)


# Задача 36:
#  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# num_rows = int(input('rows: '))
# num_cols = int(input('cols: '))
#
# operation = lambda x, y: x * y
#
#
# def print_operation_table(operation, cols, rows):
#     for cols in range(1, cols + 1):
#         for rows in range(1, rows + 1):
#             print(operation(cols, rows), end='\t')
#         print()
#
#
# print_operation_table(operation, 6, 6)
#
#
# # def function(x, y):
# #     operation = input('Введите операцию +, -, /, *: ')
# #     while True:
# #         if operation == '*':
# #             temp = x * y
# #             break
# #         if operation == '/':
# #             temp = x / y
# #             break
# #         if operation == '+':
# #             temp = x + y
# #             break
# #         if operation == '-':
# #             temp = x - y
# #             break
# #         else:
# #             print('Такой операции не существует!')
# #             break
# #     return temp
