import random

class Bot:

<<<<<<< HEAD
    # Decide ação automaticamente
    def make_move(self, current_max, player_action):

        # Pega valores das cartas
        ranks = [card.rank for card in self.hand]

        # Verifica se tem par
        if len(ranks) != len(set(ranks)):
            hand_strength = 2  # mão forte
        else:
            hand_strength = 0  # mão fraca

        bluff_chance = 0.0

        # Ajusta chance de blefe
        if hand_strength == 0:
            if player_action == "check":
                bluff_chance = 0.3
            elif player_action == "raise":
                bluff_chance = 0.1
        else:
            bluff_chance = 0.05

        # Decide ação
        if hand_strength >= 2:
            action = random.choices(["call", "raise"], weights=[0.3, 0.7])[0]
        else:
            if random.random() < bluff_chance:
                action = "raise"
            else:
                if current_max > self.current_bet:
                    action = random.choice(["call", "fold"])
                else:
                    action = "check"
=======
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
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee

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
<<<<<<< HEAD
            self.last_action = "check"
=======
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
            return 0, "check"

        # CALL
        if action == "call":
            amount = current_max - self.current_bet
<<<<<<< HEAD
            if amount > self.balance:
                amount = self.balance

            self.balance -= amount
            self.current_bet += amount

            print(f"{self.name} deu call de R${amount}")
            self.last_action = "call"
            return amount, "call"

        elif action == "raise":
            raise_amount = random.randint(1, min(5, self.balance))

            total = (current_max - self.current_bet) + raise_amount

            if total > self.balance:
                total = self.balance

            self.balance -= total
            self.current_bet += total

            print(f"{self.name} deu raise de R${total}")
            self.last_action = "raise"
            return total, "raise"

        elif action == "fold":
            print(f"{self.name} desistiu da rodada")
            self.last_action = "fold"
            return 0, "fold"
=======
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
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
