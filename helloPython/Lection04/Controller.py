
import Model as Mod_s
import Model_div as Mod_d
import Model_mult as Mod_m
import Model_sub
import View

def button_click():
    value_a = View.get_value()
    value_b = View.get_value()
    a = (input('Какое действие? '))
    if a=='+': 
        Mod_s.init(value_a, value_b)
        result = Mod_s.do_it()
        View.view_data(result)
    elif a=='/':
        Mod_d.init(value_a, value_b)
        result = Mod_d.do_it()
        View.view_data(result)
    elif a=='*':
        Mod_m.init(value_a, value_b)
        result = Mod_m.do_it()
        View.view_data(result)
    else:
        Model_sub.init(value_a, value_b)
        result = Model_sub.do_it()
        View.view_data(result)
    