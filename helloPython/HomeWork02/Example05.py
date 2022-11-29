#Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list)
list.reverse()         # Переворачиваем
print(list)
random.shuffle(list)   # Перемешиваем
print(list)
list.sort()            # Сортирую обратно
print(list)