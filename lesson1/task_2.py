"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

words = [word_1, word_2, word_3]

for line in words:
    print(f'Тип - {type(line)} | Длина - {len(line)} | Содержимое - {line} ')