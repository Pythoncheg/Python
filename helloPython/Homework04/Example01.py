
# Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415 

import math

def roundingPi(x):
    return round(math.pi, x)

def findCur(x):
    return len(x)-2


cur = input('Введите точность в формате "0.001": ')
fin = findCur(cur)
print(f'- при d = {cur}, π = {roundingPi(fin)}')

