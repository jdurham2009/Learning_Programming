#Set Player class
#Define setting a bet
#define fold
#define


class Player:
    def __init_(self, name, chips=1000):
        self.name = name
        self.hand = []
        self.current_bet = 0
        self.has_folded = False

    def place_bet(self, amount):
        if amount > self.chips:
            print(f"{self.name} does not have enough chips")
            return False
        self.chips -= amount
        self.amount += amount
        return True
    
    def fold(self):
        self.has_folded = True

    def reset_for_round(self):
        self_hand = []
        self.current_bet = 0
        self.has_folded = False
