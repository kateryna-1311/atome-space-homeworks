#task one "логінування користувача"
user_name_and_surname = input("Введіть ваше повне ім'я через пробіл: ")
#.title() переводить кожне перше слово у списку у верхній регістр
user_name_and_surname_title = user_name_and_surname.title()
# .split() роздліяє строку на окремі слова або списки, відділяє її певним обраним знаком і повертає як список
user_name_and_surname_title_list = user_name_and_surname_title.split()

if not user_name_and_surname_title_list:
    print("помилка, ви не ввели ваше повне ім'я")
else: 
#for перебирає елементи у списку
#.join() об'єднує елементи списку в одну строку за вказаним роздаленням
    user_initials = " ".join([word[0] for word in user_name_and_surname_title_list])
    print(f"Ініціали: {user_initials}")

    
# task two "Маскування email"

user_email = input("Заповніть інофрмацію про свою пошту: ")

if not user_email:
    print("помилка, ви не ввели вашу пошту")
elif user_email[-4:] != ".com" and user_email[-4:] != ".org":
    print("ви ввели не правильний домен")
else:
    user_email_name, user_domain = user_email.split("@")

    if len(user_email_name) > 2:
        #виділяє перший і останній елемент ім'я користувача, рахує решту символів й змінює їх на *
        masked_user_email_name = user_email_name[0] + "*"*(len(user_email_name)-2) + user_email_name[-1]                                                                                             
    print(f"{masked_user_email_name}@{user_domain}")


# task 3 Додавання унікального значення (створи свій set())

registered_values = {1,2,3,4,5}
user_number = int(input("Яке число ви хочете додати?: "))

if user_number in registered_values:
    print("Ось як виглядає список до змін:", registered_values)
    print("Це число вже існує, залишаємо список як є: ", registered_values)
    
else:
    print("Ось як виглядає список до змін:", registered_values)
    registered_values.add(user_number)
    print("Змінили список, тепер він виглядає так: ", registered_values)


# task 4 Аналіз тегів (set + union/intersection)

empty_set_for_first_user = set()
empty_set_for_second_user = set()

interests_of_first_user = input("Введіть свої три інтереси:")
if not interests_of_first_user:
    print("помилка, ви не ввели свої інтереси")
else:
    interests1 = interests_of_first_user.split(",")
    if len(interests1) != 3:
        print("ви ввели не ту кількість інтересів")

interests_of_second_user = input("Введіть свої три інтереси:")
if not interests_of_second_user:
    print("помилка, ви не ввели свої інтереси")
else:
    interests2 = interests_of_second_user.split(",")
    if len(interests2) != 3:
        print("ви ввели не ту кількість інтересів")

tags_of_first_user = interests_of_first_user.split(",")
tags_of_second_user = interests_of_second_user.split(",")

empty_set_for_first_user.update(tags_of_first_user)
empty_set_for_second_user.update(tags_of_second_user)

print(f"Теги першого користувача: {interests_of_first_user}")
print(f"Теги другого користувача: {interests_of_second_user}")
print(f"Спільні: {empty_set_for_first_user&empty_set_for_second_user}")
print(f"Унікальні: {empty_set_for_first_user^empty_set_for_second_user}")


#task 5 Обробка рядка з числами

user_numbers = input("Введіть числа через пробіл: ")

user_numbers_list = user_numbers.split()
sum_of_first_three_numbers = 0
list_of_only_numbers = []
for i in range(len(user_numbers_list)):
    #.isdigit() повертає True, якщо рядок складається лише з цифр.
    if user_numbers_list[i].isdigit():
        list_of_only_numbers.append(int(user_numbers_list[i]))
    else:
        print(f"Помилка: {user_numbers_list[i]} не є числом")
        break
if len(user_numbers_list) == len(list_of_only_numbers):
    sum_of_first_three_numbers = list_of_only_numbers[0] + list_of_only_numbers[1] +list_of_only_numbers[2] 
    print(f"Сума перших трьох чисел: {sum_of_first_three_numbers}")