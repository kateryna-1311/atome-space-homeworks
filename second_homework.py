#task one "логінування користувача"
user_full_name = input("Введіть ваше повне ім'я через пробіл: ")
#.title() переводить кожне перше слово у списку у верхній регістр
user_full_name = user_full_name.title()
# .split() роздліяє строку на окремі слова або списки, відділяє її певним обраним знаком і повертає як список
user_full_name = user_full_name.split()

if not user_full_name:
    print("помилка, ви не ввели ваше повне ім'я")
else: 
#for перебирає елементи у списку
#.join() об'єднує елементи списку в одну строку за вказаним роздаленням
    user_initials = " ".join([word[0] for word in user_full_name])
    print(f"Ініціали: {user_initials}")

    
# task two "Маскування email"

user_email = input("Заповніть інофрмацію про свою пошту: ")

if not user_email:
    print("помилка, ви не ввели вашу пошту")
elif not user_email.endswith((".com", ".org")):
    print("ви ввели не правильний домен")
else:
    user_email_name, user_domain = user_email.split("@")

    if len(user_email_name) > 2:
        #виділяє перший і останній елемент ім'я користувача, рахує решту символів й змінює їх на *
        masked_user_email_name = user_email_name[0] + "*"*(len(user_email_name)-2) + user_email_name[-1]                                                                                             
    print(f"{masked_user_email_name}@{user_domain}")


#task 3 Додавання унікального значення (створи свій set())

registered_values = [1,2,3,4,5]
user_number = int(input("Яке число ви хочете додати?: "))

print("Ось як виглядає список до змін:", registered_values)
if user_number in registered_values:
    
    print("Це число вже існує, залишаємо список як є: ", registered_values)
    
else:
    
    registered_values.append(user_number)
    print("Змінили список, тепер він виглядає так: ", registered_values)


# task 4 Аналіз тегів (set + union/intersection)

first_user_tags = set()
second_user_tags = set()

first_user_interests = input("Введіть свої три інтереси:")
if not first_user_interests:
    print("помилка, ви не ввели свої інтереси")
else:
    first_user_interests_list = first_user_interests.split(",")
    if len(first_user_interests_list) != 3:
        print("ви ввели не ту кількість інтересів")

second_user_interests = input("Введіть свої три інтереси:")
if not second_user_interests:
    print("помилка, ви не ввели свої інтереси")
else:
    second_user_interests_list = second_user_interests.split(",")
    if len(second_user_interests_list) != 3:
        print("ви ввели не ту кількість інтересів")


first_user_tags.update(first_user_interests_list)
second_user_tags.update(second_user_interests_list)

print(f"Теги першого користувача: {first_user_interests}")
print(f"Теги другого користувача: {second_user_interests}")
print(f"Спільні: {first_user_tags&second_user_tags}")
print(f"Унікальні: {first_user_tags^second_user_tags}")


#task 5 Обробка рядка з числами

user_numbers = input("Введіть числа через пробіл: ")

user_numbers_list = user_numbers.split()
three_numbers_sum = 0
only_numbers_list = []
for number in user_numbers_list:
    #.isdigit() повертає True, якщо рядок складається лише з цифр..
    if number.isdigit():
        only_numbers_list.append(int(number))
    else:
        print(f"Помилка: {number} не є числом")
        break
if len(user_numbers_list) == len(only_numbers_list):
    three_numbers_sum = sum(only_numbers_list[:3])
    print(f"Сума перших трьох чисел: {three_numbers_sum}")