#Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list)
list.reverse()
print(list)
random.shuffle(list)
print(list)
list.sort()
print(list)