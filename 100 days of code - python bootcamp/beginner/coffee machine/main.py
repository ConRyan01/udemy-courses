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

is_on = True
money = 0.

def report() -> str:
    """returns a print statement of the resources and money in the coffee machine"""

    return print(f'water: {resources["water"]}ml\nmilk: {resources["milk"]}ml\ncoffee: {resources["coffee"]}g\nmoney: ${money}')

def resource_check(order:dict) -> bool:
    """takes in the order dictionary to check that there are sufficient resources in the coffee machine to make the selected beverage"""

    check = True
    order_water = MENU[order]["ingredients"]["water"]
    order_coffee = MENU[order]["ingredients"]["coffee"]
    if "milk" in MENU[order]["ingredients"]:
        order_milk = MENU[order]["ingredients"]["milk"]
    
    remaining_water = resources["water"] - order_water
    remaining_coffee = resources["coffee"] - order_coffee
    if "milk" in MENU[order]["ingredients"]:
        remaining_milk = resources["milk"] - order_milk

    if remaining_water < 0:
        check = False
        print('Sorry, there is not enough water.')
    
    if remaining_coffee < 0:
        check = False
        print('Sorry, there is not enough coffee')

    if "milk" in MENU[order]["ingredients"]:
        if remaining_milk < 0:
            check = False
            print('Sorry, there is not enough milk')
    
    return check

def process_coins(order:dict) -> bool:
    """takes in the user order dictionary and prompts for int inputs for inserted change,
    checks for sufficient input, and returns a bool"""

    global money
    check = True
    inserted_quarters = int(input('Please enter how many quarters you will insert: '))
    inserted_dimes = int(input('Please enter how many dimes you will insert: '))
    inserted_nickles = int(input('Please enter how many nickles you will insert: '))
    inserted_pennies = int(input('Please enter how many pennies you will insert: '))
    total_inserted = (inserted_quarters * 0.25) + (inserted_dimes * 0.10) + (inserted_nickles * 0.05) + (inserted_pennies * 0.01)
    
    if total_inserted >= MENU[order]['cost']:
        change = total_inserted - MENU[order]['cost']
        if change == 0:
            print('transaction successful')
            money += total_inserted
        elif change > 0:
            print(f'transaction successful. Please take your change (${round(change, 2)})')
            money += (total_inserted - change)
    else:
        print('Insufficient funds. Money refunded.')
        check = False
    
    return check

def make_coffee(order:dict) -> str:
    if 'milk' in MENU[order]['ingredients']:
        required_milk = MENU[order]['ingredients']['milk']
    required_water = MENU[order]['ingredients']['water']
    required_coffee = MENU[order]['ingredients']['coffee']

    if 'milk' in MENU[order]['ingredients']:
        resources["milk"] = resources["milk"] - required_milk
    resources["coffee"] = resources["coffee"] - required_coffee
    resources["water"] = resources["water"] - required_water

    return print(f'Here is your {order}. Enjoy!')

while is_on:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if user_choice == 'off':
        is_on = False
        break
    elif user_choice == 'report':
        report()
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        if resource_check(user_choice) and process_coins(user_choice):
            make_coffee(user_choice)
    else:
        print('Invalid selection.')
            
print('Powering off... Goodbye!')
