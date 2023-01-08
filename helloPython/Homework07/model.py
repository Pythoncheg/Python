
def new_contact():
    x = input("Введите данные: ")
    return x


def find_contact():
    with open("helloPython/Homework07/base.txt", 'r') as file:
        a = file.readlines()
        print('Кого ищем?(можно указать часть номера или имени): ')
        find = input()
        return " ".join(i for i in a if find in i)


# print(find_contact())
# new_contact()
