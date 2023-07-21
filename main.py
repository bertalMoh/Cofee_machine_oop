from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Money_Machine=MoneyMachine()
coofee=CoffeeMaker()
menu=Menu()

is_On=True
while is_On==True :
    options=menu.get_items()
    wanted=input(f"What would you like? {options} : ").lower()
    if wanted=="off" :
        is_On=False
    elif wanted=="report":
        #TODO 1: print a ropport .
        coofee.report()
        Money_Machine.report()
    else :
        drink=menu.find_drink(wanted)
        # TODO 2:check if resources are suffissiants.
        if coofee.is_resource_sufficient(drink)==True:
            #TODO 3: Process coins
            #TODO 4: Check transaction succesful or not
            if Money_Machine.make_payment(drink.cost) ==True :
                #TODO 5:  Make Coffee
                coofee.make_coffee(drink)




