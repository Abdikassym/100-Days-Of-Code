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


def show_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def insert_money():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    quarters_amount = quarters * 0.25
    dimes_amount = dimes * 0.1
    nickels_amount = nickels * 0.05
    pennies_amount = pennies * 0.01
    total_amount = quarters_amount + dimes_amount + nickels_amount + pennies_amount
    return round(total_amount, 1)


def purchase(money_amount, coffee_type):
    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    money_amount -= MENU[coffee_type]['cost']
    print(f"Here is {round(money_amount, 2)} in change.")
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


def is_enough_money(money_amount, coffee_type):
    if money_amount < MENU[coffee_type]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


coffee_machine_is_on = True

while coffee_machine_is_on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print("Please insert coins.")

    if coffee == "report".lower():
        show_resources()
    else:
        coins = insert_money()
        if is_enough_money(money_amount=coins, coffee_type=coffee):
            purchase(money_amount=coins, coffee_type=coffee)
