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


money = 0

#TODO 3: Write a function to obtain users coins value
def user_coins(quarter,dime, nickel, penny):
    """This function returns the total users coins"""
    coins = {'quarter_coin': 0.25, 'nickel_coin': 0.05, 'dime_coin': 0.10, 'penny_coin': 0.01}
    total_amount = ((quarter * coins['quarter_coin']) + (dime * coins['dime_coin']) + (nickel * coins['nickel_coin']) + (penny * coins['penny_coin']))
    return round(total_amount,2)


#TODO 4: Check for resource sufficiency

def check_ingredient(drink):
    """Returns True if resources are sufficient, otherwise returns an error message."""
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            return f"Sorry, there is not enough {item}."

    return True

def deduct_resources(drink):
    """Deducts ingredients from resources after successful purchase."""
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount
        print(item, amount)

while True:
# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')
        continue
#TODO 2: Turn off the Coffee Machine when the user enters 'Off'
    elif prompt == "off":
        break

    elif prompt in MENU:
        # Check resources
        check = check_ingredient(prompt)
        if check != True:
            print(check)
            continue


        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        users_coins = user_coins(quarters,dimes,nickels, pennies)
        drink_cost = MENU[prompt]["cost"]
        balance = round((users_coins - drink_cost),2)

# TODO 5: Check the coins loaded by the user before a successful transaction
        if users_coins < drink_cost:
            print("Sorry, insufficient coins. Money refunded.")
            continue
        deduct_resources(prompt)
        money += drink_cost

        print(f'Here is your {prompt}! Enjoy!!!')
        if balance > 0:
            print(f'Please take your {balance} balance from the outlet')


    else:
        print("Sorry, Enter a valid option.")
        continue


