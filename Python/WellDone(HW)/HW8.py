# Урок 8. Работа с файлами
#
# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# text = 'article.txt'
# def chec_lines():
#     while True:
#         try:
#             lines = int(input('Введите номер строки: '))
#             if lines > 0:
#                 return lines
#         except:
#             print('Введите положительное число!')
#
# def read_file(file):
#     new_list = []
#     with open(file, 'r', encoding='utf-8') as file_new:
#         for i in file_new.read().splitlines():
#             new_list.append(i)
#         return list(new_list.__reversed__())
# def print_list(lines, listi):
#     for i in range(0, lines, 1):
#         print(listi[i])
#
# print_list(chec_lines(), read_file(text))


# 2. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).

# text = 'article.txt'
#
#
# def read_converter(file):
#     new_list = []
#     with open(file, 'r', encoding='utf-8') as new_file:
#         for i in new_file.read().split():
#             new_list.append(i)
#         return new_list
#
# def count_max(list):
#     data = list
#     temp = 0
#     word_temp = []
#     for num in list:
#         if temp <= len(num):
#             temp = len(num)
#
#     for num in list:
#         if len(num) == temp:
#             word_temp.append(num)
#     print(word_temp)
#
#
# count_max(read_converter(text))

# 3. ДОП ЗАДАЧА.
# Классическая задача про бассейн, который заполняется через 3 трубы, слишком проста. У нас труб будет больше.
# Бассейн можно заполнить из N труб. В файле pipes.txt записаны времена заполнения всего бассейна только одной
# данной работающей трубой (в часах). Затем после пустой строки перечислены трубы, которые будут заполнять бассейн.
# Сколько минут на это потребуется?
# Номер трубы соответствует номеру строки, в которой записана ее производительность.
# Результат запишите в файл time.txt

text = 'pipes.txt'

# def open_read_file(file):
#     with open(file, 'r', encoding='utf-8') as data:
#         list = []
#         for line in data:
#             list.append(line.strip())
#             print(list)

# with open(text) as f:
#   for line in f:
#     if not line.strip():
#       break
#     print(line)

with open(text, 'r') as f:
  lines = f.readlines()
  for line in lines:
    if line.strip():  # Skip empty lines
      print(line)
# open_read_file(text)

# Пример
# Ввод
# 1
# 2
# 3
# (пустая строка)
# 1 2 3
#
# Вывод
# 32.72727272727273