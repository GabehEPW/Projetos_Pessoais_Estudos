class Player:

    def __init__(self, name, balance=25):
        self.name = name
<<<<<<< HEAD
        self.hand = []            # Cartas do jogador
        self.balance = balance    # Dinheiro
        self.current_bet = 0      # Aposta atual na rodada
        self.last_action = None   # Última ação (IMPORTANTE)
=======
        self.hand = []
        self.balance = balance
        self.current_bet = 0
        self.last_action = None
        self.active = True  # Se ainda está na rodada
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee

    def receive_card(self, card):
        self.hand.append(card)

<<<<<<< HEAD
    # Mostra as cartas na tela
=======
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
    def show_hand(self):
        print(f"\nCartas de {self.name}:")
        for card in self.hand:
            print(f" - {card}")

    def reset_round(self):
        # Reseta para nova rodada
        self.hand = []
        self.current_bet = 0
        self.active = True

<<<<<<< HEAD
    # Jogador faz uma ação
    def make_bet(self, current_max):
        print(f"\nSaldo: R${self.balance}")
        print(f"Aposta atual na mesa: R${current_max}")
        print("Escolha uma ação: check, call, raise, fold")

        action = input("> ").lower()

        # CHECK → passa a vez se ninguém apostou
=======
    def make_bet(self, current_max):
        print(f"\nSaldo: R${self.balance}")
        print(f"Aposta atual: R${current_max}")
        print("Ação: check, call, raise, fold")

        action = input("> ").lower()

        # CHECK
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
        if action == "check":
            if current_max > self.current_bet:
                print("Não pode dar check!")
                return self.make_bet(current_max)

<<<<<<< HEAD
            print(f"{self.name} deu check")
            self.last_action = "check"
            return 0, "check"

        # CALL → iguala a aposta atual
        elif action == "call":
            amount = current_max - self.current_bet

            if amount > self.balance:
                amount = self.balance  # aposta tudo se não tiver saldo suficiente

            self.balance -= amount
            self.current_bet += amount

            print(f"{self.name} deu call de R${amount}")
            self.last_action = "call"
            return amount, "call"

        # RAISE → aumenta a aposta
        elif action == "raise":
            while True:
                try:
                    raise_amount = int(input("Quanto deseja apostar a mais? R$"))

                    total = (current_max - self.current_bet) + raise_amount

                    if total > self.balance:
                        print("Saldo insuficiente!")
                    else:
                        self.balance -= total
                        self.current_bet += total

                        print(f"{self.name} deu raise de R${total}")
                        self.last_action = "raise"
                        return total, "raise"

                except:
                    print("Digite um número válido!")

        # FOLD → desiste da rodada
        elif action == "fold":
            print(f"{self.name} desistiu da rodada")
            self.last_action = "fold"
            return 0, "fold"
=======
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
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee

        else:
            print("Ação inválida!")
            return self.make_bet(current_max)