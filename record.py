from name import Name
from phone import Phone
from typing import List
from birthday import Birthday


class Record:

    def __init__(self, name):
        self.name: Name = Name(name)
        self.phones: List[Phone] = []
        self.birthday: Birthday = None

    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if not new_phone.value:
            print("Phone format is not valid")
            return

        if not self.find_phone(new_phone.value):
            self.phones.append(new_phone)
        else:
            print("Phone already exists")

    def remove_phone(self, phone: str):
        entered_phone = Phone(phone)
        if not entered_phone.value:
            print("Phone format is not valid")
            return

        phone_to_remove = self.find_phone(entered_phone.value)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            print("Phone removed successfully")
        else:
            print("Phone does not exist")

    def edit_phone(self, current_phone: str, new_phone: str):
        current = Phone(current_phone)
        new = Phone(new_phone)
        updated = None
        if not current.value or not new.value:
            print("Phone format is not valid")
            return updated

        if current.value == new.value:
            print("Entered phones are equal")
            return updated

        if self.find_phone(new.value):
            print("New phone already exists")
            return updated

        if self.find_phone(current.value):
            phones = [phone.value for phone in self.phones]
            index = phones.index(current.value)
            self.phones[index] = new.value
            updated = new.value
        else:
            print("Phone does not exist")

        return updated

    def find_phone(self, phone: str):
        found_phone = None
        phones = [phone.value for phone in self.phones]
        if phone in phones:
            index = phones.index(phone)
            found_phone = self.phones[index]
        return found_phone

    def add_birthday(self, new_birthday: str):
        self.birthday = Birthday(new_birthday)

    def __str__(self):
        return (f"Contact name: {self.name.value}, "
                f"phones: {'empty' if len(self.phones) == 0 else '; '.join(str(p) for p in self.phones)}, "
                f"birthday: {'unknown' if not self.birthday else self.birthday.value}")
