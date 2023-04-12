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
