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
    "money": 0
}

machine_state_on = True

def check_resources_sufficient(customer_order):
    if resources['water'] < MENU[customer_order]['ingredients']['water']:
        return f"Sorry there is not enough water."
    elif resources['coffee'] < MENU[customer_order]['ingredients']['coffee']:
        return f"Sorry there is not enough coffee."
    elif 'milk' in MENU[customer_order]['ingredients'] and resources['milk'] < MENU[customer_order]['ingredients']['milk']:
        return f"Sorry there is not enough milk."
    else:
        return ""

def make_coffee(customer_order):
    resources['water'] = resources["water"] - MENU[customer_order]['ingredients']['water']
    resources['coffee'] = resources["coffee"] - MENU[customer_order]['ingredients']['coffee']
    if 'milk' in MENU[customer_order]['ingredients']:
        resources['milk'] = resources["milk"] - MENU[customer_order]['ingredients']['milk']
    return f"Here is your {customer_order}. Enjoy!"

def process_coins(customer_order):
    # Remember quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    customers_total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    cost_paid = False
    if customers_total < MENU[customer_order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif customers_total > MENU[customer_order]['cost']:
        cost_paid = True
        resources['money'] += MENU[customer_order]['cost']
        change = format(customers_total - MENU[customer_order]['cost'], ".2f")
        print(f"Here is {change} dollars in change.")
    return cost_paid

def report_resources():
    return f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['money']}"

def check_resources_available():
    # Function to check if the machine has run out of any essential resources
    if resources['water'] <= 0:
        print("Sorry, the machine is out of water!")
        return False
    elif resources['coffee'] <= 0:
        print("Sorry, the machine is out of coffee!")
        return False
    elif resources['milk'] <= 0:
        print("Sorry, the machine is out of milk!")
        return False
    return True

def coffee_machine():
    global machine_state_on

    while machine_state_on and check_resources_available():
        customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if customer_order == "off":
            machine_state_on = False
            print("Turning off the machine. Goodbye!")
            return False
        elif customer_order == 'report':
            print(report_resources())
            continue

        while customer_order not in MENU:
            print("We don't have that Order.")
            customer_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        resource_check = check_resources_sufficient(customer_order)
        if resource_check == "" and process_coins(customer_order):
            print(make_coffee(customer_order))
        else:
            print(resource_check)

while machine_state_on and check_resources_available():
    coffee_machine()
