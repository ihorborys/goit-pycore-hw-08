from constants import *
from handler import (add_contact, show_all_contacts, show_contact_phones, change_contact_phone,
                     add_contact_birthday, show_contact_birthday, show_closest_birthdays, save_book)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if len(user_input) > 0:
            command, *args = parse_input(user_input)

            if command in [CLOSE, EXIT]:
                save_book()
                print("Good bye!")
                break

            if command == HELLO:
                print("How can I help you?")
            elif command == ADD:
                print(add_contact(args))
            elif command == CHANGE:
                print(change_contact_phone(args))
            elif command == PHONE:
                print(show_contact_phones(args))
            elif command == ALL:
                print(show_all_contacts())
            elif command == ADD_BD:
                print(add_contact_birthday(args))
            elif command == SHOW_BD:
                print(show_contact_birthday(args))
            elif command == BIRTHDAYS:
                print(show_closest_birthdays())
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
