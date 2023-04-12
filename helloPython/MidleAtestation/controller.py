import View
import model
import fileManager
def button_click():
    while True:
        a= View.choice_action()
        if a == 1:
            fileManager.writeFile(model.newContent())
        elif a == 2:
            View.printResult(fileManager.readFile())
        elif a == 3:
            model.delValue(View.inputing())
        elif a == 4:
            break
        elif a == 5:
            model.delAll()