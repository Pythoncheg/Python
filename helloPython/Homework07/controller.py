
import model
import View
import logger

def button_click():
    a= View.choice_action()
    if a == True:
        x = model.new_contact()
        logger.write_data(x)
    else: View.print_value(model.find_contact())