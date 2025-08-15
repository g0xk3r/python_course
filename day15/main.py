MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return round(total, 2)

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

def menu():
    next = True
    while next:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            next = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif choice in MENU:
            drink = MENU[choice]
            if check_resources(drink["ingredients"]):
                payment = process_coins()
                if payment >= drink["cost"]:
                    change = round(payment - drink["cost"], 2)
                    resources["money"] += drink["cost"]
                    print(f"Here is ${change} in change.")
                    make_coffee(choice, drink["ingredients"])
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Coffee Machine! ☕")
    menu()

main()