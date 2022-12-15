
# 5'. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy

with open('hellopython/homework04/file1.txt', 'r') as f1:
    first_polinom = f1.read()
    print(f'Первый полином: {first_polinom}')

with open('hellopython/homework04/file2.txt', 'r') as f2:
    second_polinom = f2.read()
    print(f'Второй полином: {second_polinom}')

sum_polinoms = sympy.simplify(first_polinom + '+' + second_polinom)
sum_polinoms = str(sum_polinoms)

print(f'Сумма полиномов = {sum_polinoms}')

with open('hellopython/homework04/sum.txt', 'w') as wr:
    wr.write(sum_polinoms)
