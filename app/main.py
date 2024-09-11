from singleton import Singleton
from channel import Channel
from datetime import datetime

class BidBlitz():
    def __init__(self):
        self.channel = Channel()

    def addMembers(self, name, coins, fp_member):
        self.channel.addUser(name, coins, fp_member)

    def addEvent(self, event_name, prize_name, event_date):
        if not event_date:
            event_date = datetime.now()
        else:
            event_date = datetime.strptime(str(event_date), '%m/%d/%y')
        self.channel.addEvent(event_name, prize_name, event_date)

    def registerMember(self, user_id, event_name):
        self.channel.registerMember(user_id, event_name)

    def getWinner(self, event_name):
        self.channel.declareWinner(event_name)

    def placeBids(self, user_id, event_name, amounts):
        self.channel.placeBids(user_id, event_name, amounts)

    def listWinners(self):
        self.channel.listWinners()


if __name__ == "__main__":
    print("Setting up system.....")
    system = BidBlitz()

    while(1):
        print("*"*50)
        print("1. Add Member")
        print("2. Add Event")
        print("3. Register Member")
        print("4. Place Bids")
        print("5. Get Winner")
        print("6. List Winners")
        print("7. Exit")
        print("*"*50)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            coins = int(input("Enter coins: "))
            fp_member = input("Is member? (y/n): ")
            if fp_member == 'y':
                fp_member = True
            else:
                fp_member = False
            system.addMembers(name, coins, fp_member)
        elif choice == 2:
            event_name = input("Enter event name: ")
            prize_name = input("Enter prize name: ")
            event_date = input("Enter event date (mm/dd/yy): ")
            system.addEvent(event_name, prize_name, event_date)
        elif choice == 3:
            user_id = int(input("Enter user id: "))
            event_name = input("Enter event name: ")
            system.registerMember(user_id, event_name)
        elif choice == 4:
            user_id = int(input("Enter user id: "))
            event_name = input("Enter event name: ")
            amounts = input("Enter bids: ")
            amounts = amounts.split(',')
            amounts = [int(amount) for amount in amounts]
            system.placeBids(user_id, event_name, amounts)
        elif choice == 5:
            event_name = input("Enter event name: ")
            system.getWinner(event_name)
        elif choice == 6:
            system.listWinners()
        elif choice == 7:
            break
        else:
            print("Invalid choice")



