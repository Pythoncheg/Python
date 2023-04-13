import datetime
import fileManager


def newContent():
    dt_now = datetime.datetime.now()
    dt_str = dt_now.strftime('%d-%B-%Y %H:%M')
    listValue = []
    listValue.append(input("Введите заголовок заметки: "))
    listValue.append(input("Введите содержание заметки: "))
    listValue.append(dt_str)
    print("Заметка сохранена успешно!")
    return listValue
def delValue(searchItem):
    newData = []
    currentData = fileManager.readFile()
    for row in currentData:
        print(row.values())
        if row.get('Заголовок')==searchItem:
            currentData.remove(row)
            print(f'Записка с заголовком {searchItem} успешно удалена!')
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
    newData = []
    currentData = fileManager.readFile()
    for row in currentData:
        if row.get('Заголовок')==searchItem:
            currentData.remove(row)
            a = input("Хотите изменить заголовок? Y/N: ")
            if a=='y' or a=='Y':
                newData.append(input("Введите новый заголовок:"))
            elif a=='n' or a=='N':
                newData.append(row.get('Заголовок'))
            else: print("Указывайте Y или N!")
            a = input("Хотите изменить содержание? Y/N:")
            if a=='y' or a=='Y':
                newData.append(input("Введите новое содержание:"))
            elif a!='y' or a!='Y' or a!='N' or a!='n':
                print("Укажите Y или N!")
            else: newData.append(row.get('Содержание'))
            newData.append(row.get('Дата создания'))
            print(newData)

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
