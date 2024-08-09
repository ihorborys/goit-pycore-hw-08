from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, name):
        record = Record(name)
        self[name] = record
        return record

    def find(self, name) -> Record:
        return self.get(name)

    def delete(self, name):
        if self.find(name):
            self.pop(name)
            print("Record deleted successfully")
        else:
            print("Record does not exists")

    def __str__(self):
        return ''.join(f"{record}\n" for record in self.values())
