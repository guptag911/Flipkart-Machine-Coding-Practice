from singleton import Singleton
# from app.users.users import Users
# from app.events.events import Events
# from app.bids.Bid import Bid

from users import Users
from events import Events
from bids import Bid

class Channel(Singleton):
    MAX_BIDS = 5
    __users = {}
    __events = {}
    __bids = {}
    __event_members = {}
    __event_winners = {}

    def __init__(self):
        pass

    def addUser(self, name, coins, fp_member):
        try:
            user = Users(name, coins, fp_member)
            self.__users[user.id] = user
            return self.__users[user.id]
        except Exception as e:
            print(e)
            return
    
    def addEvent(self, event_name, prize_name, event_date):
        if event_name in self.__events:
            print("Event already exists")
            return
        try:
            event = Events(event_name, prize_name, event_date)
            self.__events[event_name] = event
            self.__event_winners[event_name] = None
        except Exception as e:
            print(e)
            return

    def registerMember(self, user_id, event_name):
        if user_id not in self.__users:
            print("User does not exist")
            return
        if not self.__users[user_id].fp_member:
            print("Event only for Flipkart Plus members")
            return
        if event_name not in self.__events:
            print("Event does not exist")
            return
        if event_name in self.__event_members[event_name]:
            print("User already registered for event")
            return
        self.__event_members[event_name].append(user_id)
    
    def placeBids(self, user_id, event_name, amounts):
        if user_id not in self.__users:
            print("User does not exist")
            return
        if event_name not in self.__events:
            print("Event does not exist")
            return
        if user_id not in self.__event_members[event_name]:
            print("User already registered for event")
            return
        if len(amounts)>self.MAX_BIDS:
            print(f"Max of {self.MAX_BIDS} bids can be placed")
            return
        bid_amount = sum(amounts)
        user = self.__users[user_id]
        if user.get_coins() < bid_amount:
            print("Insufficient Balance")
            return
        max_bid, min_bid = max(amounts), min(amounts)
        user.pledgeCoins(max_bid)
        curr_winner = self.__event_winners[event_name]
        if not curr_winner:
            curr_winner = {
                "bid_amount": min_bid,
                "user": user
            }
        else:
            if curr_winner["bid_amount"] < min_bid:
                curr_winner["bid_amount"] = min_bid
                curr_winner["user"] = user
        self.__event_winners[event_name] = curr_winner

    def declareWinner(self, event_name):
        if event_name not in self.__events:
            print("Event does not exist")
            return
        if not self.__event_winners[event_name]:
            print("No bids placed")
            return
        winner = self.__event_winners[event_name]["user"]
        print(f"Winner of {event_name} is {winner.get_name()}")
    
    def listWinners(self):
        winner_list = {}
        for event, winner in self.__event_winners.items():
            if not winner:
                winner_list[event] = "No Winner"
            else:
                winner_list[event] = winner["user"].get_name()
        return winner_list