import random

class Bot:

    def __init__(self, name, balance=25):
        self.name = name
        self.hand = []
        self.balance = balance
        self.current_bet = 0

    def receive_card(self, card):
        self.hand.append(card)

    def make_move(self, current_max, player_action):
        # Escolhe ação aleatória
        action = random.choice(["check", "call", "raise"])

        # Corrige jogada inválida
        if action == "check" and current_max > self.current_bet:
            action = "call"

        if action == "check":
            print(f"{self.name} deu check")
            return 0, "check"

        elif action == "call":
            amount = current_max - self.current_bet
            amount = min(amount, self.balance)

            self.balance -= amount
            self.current_bet += amount

            print(f"{self.name} deu call de R${amount}")
            return amount, "call"

        elif action == "raise":
            raise_amount = min(2, self.balance)
            total = (current_max - self.current_bet) + raise_amount

            self.balance -= total
            self.current_bet += total

            print(f"{self.name} deu raise de R${total}")
            return total, "raise"