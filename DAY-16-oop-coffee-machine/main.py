# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('aquamarine4')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# # table.field_names = ['Pokemon Name', 'Type']
# # table.add_row(['Pikachu', 'Electric'])
# # table.add_row(['Squirtle', 'Water'])
# # table.add_row(['Charmander', 'Fire'])
#
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# table.align = 'l'
# print(table)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
