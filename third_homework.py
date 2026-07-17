# first task "Калькулятор"


while True:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    arithmetic_operation = input("Enter the operation (+, -, *, /, **) or (Exit): ")

    if arithmetic_operation == "Exit":
        break
    elif arithmetic_operation == "+":
        result = first_number + second_number
    elif arithmetic_operation == "-":
        result = first_number - second_number
    elif arithmetic_operation == "*":
        result = first_number * second_number
    elif arithmetic_operation == "/":
        if second_number == 0:
            print("Сan't divide by zero")
            continue
        else:
            result = first_number / second_number
    elif arithmetic_operation == "**":
        result = first_number**second_number
    else:
        print("Invalid operation. Please enter one of +, -, *, /, **")
        continue
    print(f"Result: {result}")

# second task "Облік витрат за категоріями"

user_balance = float(input("Enter your balance: "))
expenses_by_category = {"Food:": 0, "Games": 0}
print(expenses_by_category)

while True:
    category = input("Select the category you spent money on: ").capitalize()

    if category == "Exit":
        break

    expense = float(input("Enter the amount of costs: "))
    if expense > user_balance:
        print("Insufficient funds")
        continue
    user_balance = user_balance - expense
    expenses_by_category[category] = expenses_by_category.get(category, 0) + expense

    print(f"Total balance {user_balance}")
    print(f"Costs by category: {expenses_by_category}")
