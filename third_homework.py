# #first task "Калькулятор"

user_maths_operation = "none"
while user_maths_operation != "Exit":
    user_first_number = int(input("Enter the first number: "))
    user_second_number = int(input("Enter the second number: "))
    user_maths_operation = input("Enter the operation (+, -, *, /, **) or (Exit): ")

    if user_maths_operation == "Exit":
        break
    elif user_maths_operation == "+":
        result = user_first_number + user_second_number  
    elif user_maths_operation == "-":
        result = user_first_number - user_second_number   
    elif user_maths_operation == "*":
        result = user_first_number * user_second_number        
    elif user_maths_operation == "/":
        result = user_first_number / user_second_number       
    elif user_maths_operation == "**":
        result = user_first_number ** user_second_number
        print(f"Result: {result}")
    else:
        print("Invalid operation. Please enter one of +, -, *, /, **")
    print(f"Result: {result}")

#second task "Облік витрат за категоріями"

user_balance = float(input("Enter your balance: "))
user_costs_by_category = {"Food:": 0, "Games": 0}
print(user_costs_by_category)
user_categories = "none"

while user_categories != "Exit":
    user_categories = input("Select the category you spent money on: ").capitalize()

    if user_categories == "Exit":
        break
    if user_categories not in user_costs_by_category:
        user_costs_by_category[user_categories] = 0

    user_amount_of_costs = float(input("Enter the amount of costs: "))

    if user_amount_of_costs > user_balance:
        print("Insufficient funds")
    else:
        user_balance = user_balance - user_amount_of_costs
        user_costs_by_category[user_categories] += user_amount_of_costs

    print(f"Total balance {user_balance}")
    print(f"Costs by category: {user_costs_by_category}")
