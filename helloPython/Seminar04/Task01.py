
# a = input('Select number:').split()
# print(f'max => {max(a)}, min => {min(a)}')

import sympy

x = sympy.Symbol('x')
a = input('Введите формулу: ')
print(sympy.solve(a, x))