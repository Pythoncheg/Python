import View
import model
import fileManager
from operator import itemgetter
def button_click():
    View.printHelp()
    while True:
        a= View.choice_action()
        if a == 1:
            fileManager.writeFile(model.newContent())
            View.confMsg(a)
        elif a == 2:
            newList = fileManager.readFile()
            model.findValues(input("Введите дату для поиска: "), newList)
        elif a == 3:
            model.delValue(View.inputing())
            View.confMsg(a)
        elif a == 4:
            break
        elif a == 5:
            model.delAll()
            View.confMsg(a)
        elif a == 6:
            model.redactValue(View.inputing())
            View.confMsg(a)
        elif a == 7:
            newList = fileManager.readFile()
            sortList = sorted(newList, key=itemgetter('Дата создания'))
            View.printResult(sortList)
            View.confMsg(a)
        elif a == 8:
            View.printHelp()