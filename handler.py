from typing import List
from decorators import input_error
from datetime import datetime, timedelta
from record import Record
from constants import INTERVAL
from save_load import save_data, load_data

book = load_data()


@input_error
def add_contact(args: List[str]) -> str:
    name, *rest = args
    record = book.find(name)
    message = "Record already exists"
    if not record:
        record = book.add_record(name)
        message = "Record added successfully"
    if rest:
        record.add_phone(rest[0])
        message = "Record updated successfully"
    return message


def show_all_contacts() -> str:
    message = "Address book is empty"
    if book:
        message = str(book)
    return message


@input_error
def show_contact_phones(args: List[str]) -> str:
    message = "Record does not exists"
    record = book.find(args[0])
    if record:
        message = "phones: " + '; '.join(str(p) for p in record.phones)
    return message


@input_error
def change_contact_phone(args: List[str]) -> str:
    name, current_phone, new_phone = args
    message = "Record does not exists"
    record = book.find(name)
    if record:
        changed = record.edit_phone(current_phone, new_phone)
        if changed:
            message = "Phone updated successfully"
        else:
            message = "Phone update failed"
    return message


@input_error
def add_contact_birthday(args: List[str]) -> str:
    name, bd_date = args
    message = "Record does not exists"
    record = book.find(name)
    if record:
        record.add_birthday(bd_date)
        message = "Birthday added successfully"
    return message


@input_error
def show_contact_birthday(args: List[str]) -> str:
    message = "Record does not exists"
    record = book.find(args[0])
    if record:
        message = record.birthday.value
    return message


def show_closest_birthdays() -> str:
    message = "Address book is empty"
    if book:
        message = ""
        celebration_list = []
        for record in book.values():
            celebration_date = get_celebration_date(record)
            if celebration_date:
                celebration_list.append({
                    "name": record.name,
                    "date": celebration_date
                })

        if len(celebration_list) == 0:
            message = "No celebration dates available"
        else:
            celebration_list.sort(key=lambda item: item["date"])
            for contact in celebration_list:
                message += f"{contact["name"]}: {contact["date"].date()}\n"
    return message


def get_celebration_date(record: Record):
    if not record.birthday or not record.birthday.date:
        return None

    today = datetime.today()
    celebration_date = record.birthday.date.replace(year=today.year)
    final_date = today + timedelta(days=INTERVAL)
    if celebration_date < today or celebration_date > final_date:
        return None

    if celebration_date.weekday() == 5:
        celebration_date += timedelta(days=2)
    if celebration_date.weekday() == 6:
        celebration_date += timedelta(days=1)
    return celebration_date


def save_book():
    save_data(book)
