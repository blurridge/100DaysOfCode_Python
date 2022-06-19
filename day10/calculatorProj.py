# Utility Functions and Dictionary

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

def calculator_function():
    first_number = float(input("What's the first number?: "))
    continue_choice = "y"
    while continue_choice == "y":
        print("+\n-\n*\n/")
        operation_picked = input("Pick an operation: ")
        if operation_picked not in operations:
            print("You have entered an invalid operation. Calculator will be reset.")
            calculator_function()
        second_number = float(input("What's the next number?: "))
        result = operations[operation_picked](first_number, second_number)
        print(f"{first_number} {operation_picked} {second_number} = {result}")
        continue_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if continue_choice == "y":
            first_number = result
        else:
            calculator_function()

# Main Function

print(r""""
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  
""")

calculator_function()