from datetime import datetime


class Events():
    def __init__(self, name, prize, date):
        self.name = name
        self.prize = prize
        self.date = date or datetime.now()

    def get_name(self):
        return self.name
    
    def get_date(self):
        return self.date
