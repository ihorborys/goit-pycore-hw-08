from datetime import datetime
from field import Field

FORMAT = "%d.%m.%Y"


class Birthday(Field):
    def __init__(self, value):
        try:
            self.date: datetime = datetime.strptime(value, FORMAT)
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
