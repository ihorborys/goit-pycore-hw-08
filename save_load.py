import pickle
import os
from address_book import AddressBook

FILE_NAME = "addressbook.pkl"


def save_data(book):
    with open(FILE_NAME, "wb") as f:
        pickle.dump(book, f)


def load_data():
    book = AddressBook()
    if os.path.getsize(FILE_NAME) > 0:
        try:
            with open(FILE_NAME, "rb") as f:
                book = pickle.load(f)
        except FileNotFoundError:
            pass

    return book
