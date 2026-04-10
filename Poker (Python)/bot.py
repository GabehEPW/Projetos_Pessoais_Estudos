import random

class Bot:

    def __init__(self, name, balance=25):
        self.name = name
        self.hand = []
        self.balance = balance
        self.current_bet = 0
        self.active = True

    def receive_card(self, card):
        self.hand.append(card)

    def reset_round(self):
        self.hand = []
        self.current_bet = 0
        self.active = True

    def make_move(self, current_max):
        # Escolhe ação aleatória
        action = random.choice(["check", "call", "raise", "fold"])

        # Corrige check inválido
        if action == "check" and current_max > self.current_bet:
            action = "call"

        # FOLD
        if action == "fold":
            print(f"{self.name} desistiu")
            self.active = False
            return -1, "fold"

        # CHECK
        if action == "check":
            print(f"{self.name} deu check")
            return 0, "check"

        # CALL
        if action == "call":
            amount = current_max - self.current_bet
            amount = min(amount, self.balance)

            self.balance -= amount
            self.current_bet += amount

            print(f"{self.name} deu call de R${amount}")
            return amount, "call"

        # RAISE
        if action == "raise":
            raise_amount = min(2, self.balance)
            total = (current_max - self.current_bet) + raise_amount

            self.balance -= total
            self.current_bet += total

            print(f"{self.name} deu raise de R${total}")
            return total, "raise"