
def printHelp():
    print('\n Для вывода всех заметок используйте "All"\n'
          'Для создания новой заметки используйте "Add"\n'
          'Для поиска по дате используйте "Find"\n'
          'Для удаления заметки используйте "Del"\n'
          'Для выхода используйте "q"\n'
          'Для удаления всех записок используйте "Delall"\n'
          'Для редактирования записок используйте "Edit"\n'
          'Для вызова данного меню используйте "Help" или "h"')
def inputing():
    a = input()
    return a
def print_value(data):
    print(data)

def choice_action():
    while True:
        print('\nВведите команду: ')
        a=input()
        if a=='Add' or a=='add':
            return 1
        elif a=='Find' or a=='find':
            print('Читаю файл')
            return 2
        elif a=='Del' or a=='del':
            print("Укажите заголовок заметки: ")
            return 3
        elif a=='q' or a=='Q':
            print("Завершение работы...")
            return 4
        elif a=='delall' or a=='DelAll' or a=='Delall':
            print('Вы уверены, что хотите удалить ВСЕ! данные? Y/N: ')
            a = input()
            if a == 'Y' or a=='y':
                return 5
            else:
                print("Удаление НЕ выполнено.")
        elif a=='edit' or a=='Edit' or a=='EDIT':
            print("Укажите заголовок заметки: ")
            return 6
        elif a=='all' or a=='All' or a=='ALL':
            return 7
        elif a == "Help" or a == "help" or a == 'h':
            return 8
        else: print("Не верная комманда")
def confMsg(value):
    if value==1:
        print("\nЗаметка успешно добавлена.")
    elif value==2:
        print("\nКонец файла.")
    elif value==3:
        print("\nУспешно удалено.")
    elif value==5:
        print("\nФайл очищен.")
    elif value==6:
        print("\nУспешно изменено.")
def printResult(value):
    print(*value, sep="\n")