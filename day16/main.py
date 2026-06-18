from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creamos objetos
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

def ask_user():
    return input(f"What would you like? ({menu.get_items()}):")

def print_report():
    coffee_maker.report()
    money_machine.report()

def main():
    selection = True
    while selection:
        sel = ask_user().casefold()
        if sel != "off":
            if sel == "report":
                print_report()
            else:
                print(sel)
                item = menu.find_drink(sel)
                if item:
                    if coffee_maker.is_resource_sufficient(item):
                        print(f"Your {item.name} is {money_machine.CURRENCY}{item.cost}")
                        if money_machine.make_payment(item.cost):
                            print("\nBefore purchasing\n")
                            print_report()
                            print("\n")
                            coffee_maker.make_coffee(item)
                            print("\nAfter purchasing\n")
                            print_report()
        else:
            selection = False

main()