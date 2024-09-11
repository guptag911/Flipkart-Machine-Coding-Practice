class Bid():
    def __init__(self, amount, user_id, event_id):
        self.amount = amount
        self.user_id = user_id
        self.event_id = event_id
    
    def get_amount(self):
        return self.amount
    
    def get_user_id(self):
        return self.user_id
    
    def get_event_id(self):
        return self.event_id
