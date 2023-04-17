import View
import model
import fileManager
def button_click():
    while True:
        a= View.choice_action()
        if a == 1:
            fileManager.writeFile(model.newContent())
            View.confMsg(a)
        elif a == 2:
            newList = fileManager.readFile()
            # View.printResult(fileManager.readFile())
            # newList.sort(key=model.sortList())
            View.printResult(newList)
            View.confMsg(a)
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