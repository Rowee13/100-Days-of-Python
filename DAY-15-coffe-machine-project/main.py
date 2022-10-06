MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order = input('What would you like? (espresso/latte/cappuccino): ')


def process_coins():
    print("Please insert coins.")
    coins_quarter = int(input("how many quarters?: "))
    coins_dimes = int(input("how many dimes?: "))
    coins_nickels = int(input("how many nickels?: "))
    coins_pennies = int(input("how many pinnies?: "))


print("Sorry, that's not enough money. Money refunded.")


#
#
#
#
# TODO: 1 - Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
#         - Check user's input to decide what to do next
#         - The prompt above should show every time action has completed and to serve the next customer
# TODO: 2 - Turn off the coffee machine by entering "off" to the prompt
#         - For maintainers of the coffee machine, they can use "off" as the secret word to turn off the machine
# TODO: 3 - Print report
#         - When the users enters "reports" to the prompt, a report should be generated
#           that shows the current resource values e.g.
#           Water: 100ml
#           Milk: 50ml
#           Coffee: 76g
#           Money: $2.5
# TODO: 4 - Check if resources is sufficient
#         - When the user chooses a drink, the program should check if there are enough
#           resources to make that drink
#         - E.g. if latte requires 200ml water but there is only 100ml left in the machine,
#           it should not continue to make the drink and print "Sorry there is not enough water."
#         - The same should happen if another resource is depleted
# TODO: 5 - Process coins
#           Penny - 1cent, Dime - 10cents, Nickel - 5cents, Quarter - 25cents
#         - Check that the user has inserted enough money to purchase the drink they selected
#           E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#           program should say “Sorry that's not enough money. Money refunded.”.
#         - But if the user has inserted enough money, then the cost of the drink gets added to the
#           machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#           Water: 100ml
#           Milk: 50ml
#           Coffee: 76g
#           Money: $2.5
#         - If the user has inserted too much money, the machine should offer change.
#           E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
# TODO: 6 - Make Coffee
#         - If the transaction is successful and there are enough resources to make the drink the
#           user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
#           E.g. report before purchasing latte:
#           Water: 300ml
#           Milk: 200ml
#           Coffee: 100g
#           Money: $0
#           Report after purchasing latte:
#           Water: 100ml
#           Milk: 50ml
#           Coffee: 76g
#           Money: $2.5
#         - Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#           latte was their choice of drink
