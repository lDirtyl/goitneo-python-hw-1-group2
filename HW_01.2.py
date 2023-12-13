"""Завдання 2

Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.

БОТ ПОМІЧНИК ПОВИНЕН СТАТИ ДЛЯ НАС ПРОТОТИПОМ ЗАСТОСУНКУ-АСИСТЕНТА ЯКИЙ МИ РОЗРОБИМО В НАСТУПНИХ ДОМАШНІХ ЗАВДАННЯХ. ЗАСТОСУНОК-АСИСТЕНТ В ПЕРШОМУ НАБЛИЖЕННІ ПОВИНЕН ВМІТИ ПРАЦЮВАТИ З КНИГОЮ КОНТАКТІВ ТА КАЛЕНДАРЕМ.
У цій домашній роботі зосередимося на інтерфейсі самого бота.  
Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). 
CLI достатньо просто реалізувати. Будь-який CLI складається з трьох основних елементів:

Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, 
виділення з рядка ключових слів та модифікаторів команд.
Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
Цикл запит-відповідь. 
Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.
На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, 
знаходити номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. 
Щоб реалізувати таку нескладну логіку, скористаємося словником. 
У словнику будемо зберігати ім'я користувача як ключ і номер телефону як значення.

Рекомендації для виконання
По перше, нам треба систематизувати опис форматів наших команд для консольного бота-помічника. 
Це допоможе зрозуміти які функції треба зробити для кожної команди. Зробімо це:

1. Команда "hello", тут можна обійтись поки без функції та використати звичайний print:
Введення: "hello"
Вивід: "How can I help you?"

2. Команда "add [ім'я] [номер телефону]". Для цієї команди зробимо функцію add_contact:
Введення: "add John 1234567890"
Вивід: "Contact added."

3. Команда "change [ім'я] [новий номер телефону]". Для цієї команди зробимо функцію change_contact:
Введення: "change John 0987654321"
Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено

4. Команда "phone [ім'я]". Для цієї команди зробимо функцію show_phone:
Введення: "phone John"
Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено

5. Команда "all". Для цієї команди зробимо функцію show_all:
Введення: "all"
Вивід: усі збережені контакти з номерами телефонів

6. Команда "close" або "exit". Оскільки тут треба перервати виконання програми, можна поки обійтись без функції для цих команд:
Введення: будь-яке з цих слів
Вивід: "Good bye!" та завершення роботи бота

Будь-яка команда, яка не відповідає вищезазначеним форматам, буде вважатися нами невірною, 
і бот буде виводити повідомлення "Invalid command."""


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):  # Завдання 3. Зміна телефону
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):  # Завдання 4. Показати номер за ключем name
    (name,) = args
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):  # Завдання 5. Показати всі збережені контакти
    if not contacts:
        return "No contacts available."
    else:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
