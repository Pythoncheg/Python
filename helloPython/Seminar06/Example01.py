
# Задача 1

# Вводятся названия городов в одну строчку через пробел. Необходимо определить функцию map,
# которая бы возвращала названия городов только длиной более 5 символов. Вместо остальных названий -
# строку с дефисом ("-").
# Сформировать список из полученных значений и отобразить его на экране в одну строчку через пробел.

# Ввод:
# Москва Уфа Вологда Тула Владивосток Хабаровск
# Вывод:
# Москва - Вологда - Владивосток Хабаровск
from os import system
system('cls')

a = 'Москва Уфа Вологда Тула Владивосток Хабаровск'

print(" ".join(list(map(lambda x: '-' if len(x) < 5 else x, a.split()))))


