# Dictionary of Menu

coffee_menu = {
    "espresso": 
    {
        "ingredients": 
        {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": 
    {
        "ingredients": 
        {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": 
    {
        "ingredients": 
        {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Coffee Machine Config (in ml/g/$)

water_amt = 300
milk_amt = 200
coffee_amt = 100
money_amt = 0.00

# Utility Functions

def getReport():
    global money_amt
    formatted_money = "{:.2f}".format(money_amt)
    print(f"Water: {water_amt}ml\nMilk: {milk_amt}ml\nCoffee: {coffee_amt}g\nMoney: ${formatted_money}")

def changeReport(coffee_name):
    global water_amt, milk_amt, coffee_amt, money_amt
    water_amt-=coffee_menu[coffee_name]["ingredients"]["water"]
    if "milk" in coffee_menu[coffee_name]["ingredients"]:
        milk_amt-=coffee_menu[coffee_name]["ingredients"]["milk"]
    coffee_amt-=coffee_menu[coffee_name]["ingredients"]["coffee"]
    money_amt+=coffee_menu[coffee_name]['cost']

def processCoins(coffee_name):
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total_amt = float((quarter*0.25) + (dime*0.10) + (nickel*0.05) + (penny*0.01))
    if total_amt < coffee_menu[coffee_name]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        changeReport(coffee_name)
        change = round(total_amt - coffee_menu[coffee_name]['cost'], 2)
        formatted_change =  "{:.2f}".format(change)
        if change > 0:
            print(f"Here is ${formatted_change} in change.")
        print(f"Here is your {coffee_name}. Enjoy!")

def checkResources(coffee_name):
    if water_amt < coffee_menu[coffee_name]["ingredients"]["water"]:
        return "water"
    elif coffee_amt < coffee_menu[coffee_name]["ingredients"]["coffee"]:
        return "coffee"
    elif "milk" in coffee_menu[coffee_name]["ingredients"]:
        if milk_amt < coffee_menu[coffee_name]["ingredients"]["milk"]:
            return "milk"

def getCoffee(coffee_name):
    resource_lacking = checkResources(coffee_name)
    if resource_lacking == None:
        processCoins(coffee_name)
    else:
        print(f"Sorry there is not enough {resource_lacking}.")
        
# Main function

user_choice = "on"
while user_choice != "off":
    user_choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if user_choice == "report":
        getReport()
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        getCoffee(user_choice)
    elif user_choice == "off":
        print("Coffee machine powering down...")
    else:
        print("That is an invalid choice!\n")