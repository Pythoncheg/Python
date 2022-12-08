
# Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# Пример:

# [1 , 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
import random

a = [1, 5, 2, 3, 4, 6, 1, 7]


def sorting(x):
    return [x[i] for i in range(0, 7) if x[i] < x[i+1]]
    # b =[]
    # for i in range(len(x)):
    #     if x[i] <= x[i+1]:
    #         b.append(x[i])
    #     else:
    #         b.append(x[i])
    #         return b


print(sorting(a))
