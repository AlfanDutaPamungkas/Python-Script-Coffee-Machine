from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_list = menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    prompt = input(f"What would you like? ({menu_list}): ").lower()
    if prompt == "off":
        break
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        order = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    else:
        menu.find_drink(prompt)