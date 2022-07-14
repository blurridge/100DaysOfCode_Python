# Main

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
user_choice = "on"
while user_choice != "off":
    drink_options = menu.get_items()
    user_choice = input(f"What would you like? {drink_options}: ").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice != "off":
        drink = menu.find_drink(user_choice)
        if drink != None:
            cost = drink.cost
            is_enough = coffee_maker.is_resource_sufficient(drink)
            if is_enough == True:
                is_payment_good = money_machine.make_payment(cost)
                if is_payment_good == True:
                    coffee_maker.make_coffee(drink)