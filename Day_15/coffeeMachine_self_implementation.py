MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

machine_state_on = True

def check_resources_sufficient(drink):
    """Checks if the machine has enough resources to make the drink."""
    if resources['water'] < drink['ingredients'].get('water', 0):
        return f"Sorry there is not enough water."
    elif resources['coffee'] < drink['ingredients'].get('coffee', 0):
        return f"Sorry there is not enough coffee."
    elif 'milk' in drink['ingredients'] and resources['milk'] < drink['ingredients'].get('milk', 0):
        return f"Sorry there is not enough milk."
    else:
        return ""

def make_coffee(drink_name, drink):
    """Deducts the resources used to make the drink and serves it."""
    resources['water'] -= drink['ingredients'].get('water', 0)
    resources['coffee'] -= drink['ingredients'].get('coffee', 0)
    if 'milk' in drink['ingredients']:
        resources['milk'] -= drink['ingredients'].get('milk', 0)
    return f"Here is your {drink_name}. Enjoy!"

def process_payment(drink):
    """Handles payment and checks if enough money has been inserted."""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    customers_total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    cost_paid = False

    if customers_total < drink["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        cost_paid = True
        resources['money'] += drink['cost']
        if customers_total > drink['cost']:
            change = format(customers_total - drink['cost'], ".2f")
            print(f"Here is {change} dollars in change.")
    return cost_paid

def report_resources():
    """Prints the current resource levels."""
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}"

def check_resources_available():
    """Checks if the machine is out of any essential resources."""
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
    """Main function to run the coffee machine."""
    global machine_state_on

    while machine_state_on and check_resources_available():
        customer_order = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

        if customer_order == "off":
            machine_state_on = False
            print("Turning off the machine. Goodbye!")
            return False
        elif customer_order == 'report':
            print(report_resources())
            continue

        if customer_order not in MENU:
            print("We don't have that order.")
            continue

        # Use drink to avoid repeated MENU lookups
        drink = MENU[customer_order]

        resource_check = check_resources_sufficient(drink)
        if resource_check == "":
            if process_payment(drink):
                print(make_coffee(customer_order, drink))
        else:
            print(resource_check)

# Start the coffee machine
while machine_state_on and check_resources_available():
    coffee_machine()
