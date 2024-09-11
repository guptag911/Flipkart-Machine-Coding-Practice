from datetime import datetime


class Users():
    def __init__(self, name, coins, fp_member=True):
        if not self.__validateCoins(coins):
            raise ValueError("Coins must be greater than 0")
        self.id = int(datetime.now().timestamp() * 1000)
        self.name = name
        self.coins = coins
        self.fp_member = fp_member

    def get_name(self):
        return self.name

    def get_coins(self):
        return self.coins

    def get_fp_member(self):
        return self.fp_member

    def pledgeCoins(self, amount):
        if amount > self.coins:
            raise ValueError("Insufficient Balance")
        self.coins -= amount    

    def __validateCoins(self, coins):
        if coins <= 0:
            return False
        return True
