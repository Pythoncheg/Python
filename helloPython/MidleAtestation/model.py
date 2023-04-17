import datetime
import fileManager
import View


def newContent():
    dt_now = datetime.datetime.now()
    dt_str = dt_now.strftime('%d-%B-%Y %H:%M')
    listValue = []
    listValue.append(input("Введите заголовок заметки: "))
    listValue.append(input("Введите содержание заметки: "))
    listValue.append(dt_str)
    return listValue
def delValue(searchItem):
    newData = []
    currentData = fileManager.readFile()
    for row in currentData:
        if row.get('Заголовок') == searchItem:
            currentData.remove(row)
    flag=True
    for row in currentData:
        newData.append(row.get('Заголовок'))
        newData.append(row.get('Содержание'))
        newData.append(row.get('Дата создания'))
        if flag==True:
            fileManager.writeFileAfterDel(newData)
            flag=False
        else:
            fileManager.writeFile(newData)
        newData = []
    return newData

def delAll():
    fileManager.writeEmptyFile()
def redactValue(searchItem):
    editData = []
    currentData = fileManager.readFile()
    for row in currentData:
        if row.get('Заголовок')==searchItem:
            a = input("Хотите изменить заголовок? Y/N: ")
            if a=='y' or a=='Y':
                editData.append(input("Введите новый заголовок:"))
            elif a=='n' or a=='N':
                editData.append(row.get('Заголовок'))
            else:
                print("Указывайте Y или N!")
                redactValue(searchItem)
            a = input("Хотите изменить содержание? Y/N:")
            if a=='y' or a=='Y':
                editData.append(input("Введите новое содержание:"))
            elif a=='n' or a=='N':
                editData.append(row.get('Содержание'))
            else:
                print("Укажите Y или N!")
                redactValue(searchItem)
            editData.append(row.get('Дата создания'))
            currentData.remove(row)
    d=True
    for rows in currentData:
        newData = []
        newData.append(rows.get('Заголовок'))
        newData.append(rows.get('Содержание'))
        newData.append(rows.get('Дата создания'))
        if d==True:
            fileManager.writeFileAfterDel(newData)
            d=False
        else:
            fileManager.writeFile(newData)
    fileManager.writeFile(editData)

def findValues(searchValues, list):
    count=0
    for row in list:
        if row.get('Дата создания').startswith(searchValues):
            View.print_value(row)
            count+=1

    if count == 0:
        print("\nНет записей с такой датой!")
    else:
        print(f"\nКол-во найденых заметок: {count}")