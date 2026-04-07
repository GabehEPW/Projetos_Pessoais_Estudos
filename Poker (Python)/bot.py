import random
from player import Player

class Bot(Player):

    # Bot faz aposta automaticamente
    def make_move(self, current_max):
        # Decide aleatoriamente
        action = random.choice(["check", "call", "raise"])
        
        # Check
        if action == "check":
            if current_max > self.current_bet:
                # Não pode dar check se alguém apostou
                action = "call"
            else:
                print(f"{self.name} deu check")
                return 0

        # Call
        if action == "call":
            amount = current_max - self.current_bet
            if amount > self.balance:
                amount = self.balance
            self.balance -= amount
            self.current_bet += amount
            print(f"{self.name} deu call de R${amount}")
            return amount

        # Raise
        if action == "raise":
            raise_amount = random.randint(1, self.balance)
            total = (current_max - self.current_bet) + raise_amount
            if total > self.balance:
                total = self.balance
            self.balance -= total
            self.current_bet += total
            print(f"{self.name} deu raise de R${total}")
            return total