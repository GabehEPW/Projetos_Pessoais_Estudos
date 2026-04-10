class Player:

    def __init__(self, name, balance=25):
        self.name = name
        self.hand = []
        self.balance = balance
        self.current_bet = 0
        self.last_action = None
        self.active = True  # Se ainda está na rodada

    def receive_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(f"\nCartas de {self.name}:")
        for card in self.hand:
            print(f" - {card}")

    def reset_round(self):
        # Reseta para nova rodada
        self.hand = []
        self.current_bet = 0
        self.active = True

    def make_bet(self, current_max):
        print(f"\nSaldo: R${self.balance}")
        print(f"Aposta atual: R${current_max}")
        print("Ação: check, call, raise, fold")

        action = input("> ").lower()

        # CHECK
        if action == "check":
            if current_max > self.current_bet:
                print("Não pode dar check!")
                return self.make_bet(current_max)

            self.last_action = "check"
            return 0

        # CALL
        elif action == "call":
            amount = current_max - self.current_bet
            amount = min(amount, self.balance)

            self.balance -= amount
            self.current_bet += amount

            self.last_action = "call"
            return amount

        # RAISE
        elif action == "raise":
            try:
                raise_amount = int(input("Aumentar quanto? R$"))
                total = (current_max - self.current_bet) + raise_amount

                if total > self.balance:
                    print("Saldo insuficiente!")
                    return self.make_bet(current_max)

                self.balance -= total
                self.current_bet += total

                self.last_action = "raise"
                return total
            except:
                print("Valor inválido!")
                return self.make_bet(current_max)

        # FOLD
        elif action == "fold":
            print(f"{self.name} desistiu!")
            self.active = False
            self.last_action = "fold"
            return -1

        else:
            print("Ação inválida!")
            return self.make_bet(current_max)