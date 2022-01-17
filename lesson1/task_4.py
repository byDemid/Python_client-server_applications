"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

words = [word_1, word_2, word_3, word_4]

words_b = []
words_str = []

for line in words:
    line = line.encode('UTF-8')
    words_b.append(line)
    print(f'\nbytes - {line}')
    line = line.decode('UTF-8')
    words_str.append(line)
    print(f'str - {line}')

print()
print(words_b)
print(words_str)

# не знаю можно ли в одном цикле или нужно записать а потмо сново , написал и так и так

# for line in words:
#     line = line.encode('UTF-8')
#     words_b.append(line)
#
# print(words_b)
#
# for line in words_b:
#     line = line.decode('UTF-8')
#     words_str.append(line)
#
# print(words_str)