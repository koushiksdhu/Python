
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

def resources_sufficient(check_ingredients):
    for item in check_ingredients:
        if check_ingredients[item] > resources[item]:
            print(f"Sorry! There is no enough {item}.")
            return False
    return True
    
def process_coins():
    print("Please insert coins: ")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.10
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total
    
def transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry! That's not enough money. Money Refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}$ in change.")
        global profit 
        profit += money_received
        return True 

def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}. Enjoy") 
    
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                                
            
            
            
            