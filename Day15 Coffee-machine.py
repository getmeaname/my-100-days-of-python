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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns true if the resources are abundant false if short on resource"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, cost_of_drink):
    """Check if transaction if successful"""
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is your ${change} change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry not enough money to process the order, here is your refund")
        return False


def process_payment():
    """Returns the total amount of money inserted"""
    print("Please insert coins.")
    total = float(input("How many quarters: ")) * 0.25
    total += float(input("How many dimes: ")) * 0.10
    total += float(input("How many nickels: ")) * 0.05
    total += float(input("How many pennies: ")) * 0.01
    return total


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_payment()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
