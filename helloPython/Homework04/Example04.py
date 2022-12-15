
# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5 = 0 
# 
import sympy
from random import randint as r

def create_polinom(k: int, simple: bool =  True):
    polinom = ' '
    for i in range(k, -1, -1):
        polinom += f'{r(0,2)}*x^{i}+'
        if i==0:
            polinom+=f'{r(0,100)}*x^{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)

def create_file(polinom, filename: str = 'new'):
    with open(f'helloPython/Homework04/{filename}.txt', 'w') as f:
        f.write(polinom)       


k = int(input("Введите коэффициент K: "))
print(create_polinom(k))
create_file(create_polinom(k), 'file2')


