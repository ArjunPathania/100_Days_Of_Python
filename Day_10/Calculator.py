import os
import art

def clear_screen():
    if os.getenv('TERM'):
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("\n" * 20)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator(input1, input2, operation):
    try:
        result = operations[operation](input1, input2)
        print(f"{input1} {operation} {input2} = {result}")
        return result
    except KeyError:
        print("Error: Invalid operation.")
        return None

def main():
    print(art.logo)
    cont = "n"
    output = 0

    while True:
        if cont == "y":
            a = output
            operation = input("Pick an operation (+, -, *, /): ")
            try:
                b = float(input("What's the next number?: "))
                output = calculator(a, b, operation)
            except ValueError:
                print("Error: Please enter a valid number.")
                continue
        else:
            clear_screen()
            try:
                a = float(input("What's the first number?: "))
                operation = input("Pick an operation (+, -, *, /): ")
                b = float(input("What's the next number?: "))
                output = calculator(a, b, operation)
            except ValueError:
                print("Error: Please enter a valid number.")
                continue
        
        cont = input(f"Type 'y' to continue calculating with {output}, or 'n' to start a new calculation: ").lower()

if __name__ == "__main__":
    main()

