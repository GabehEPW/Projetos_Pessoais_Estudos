class Player:

    def __init__(self, name, balance=25):
        self.name = name
        self.hand = []            # Cartas do jogador
        self.balance = balance    # Dinheiro
        self.current_bet = 0      # Aposta atual na rodada
        self.last_action = None   # Última ação (IMPORTANTE)

    # Recebe uma carta
    def receive_card(self, card):
        self.hand.append(card)

    # Mostra as cartas na tela
    def show_hand(self):
        print(f"\nCartas de {self.name}:")
        for card in self.hand:
            print(card)

    # Jogador faz uma ação
    def make_bet(self, current_max):
        print(f"\nSaldo: R${self.balance}")
        print(f"Aposta atual na mesa: R${current_max}")
        print("Escolha uma ação: check, call, raise, fold")

        action = input("> ").lower()

        # CHECK → passa a vez se ninguém apostou
        if action == "check":
            if current_max > self.current_bet:
                print("Não pode dar check!")
                return self.make_bet(current_max)

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

        else:
            print("Ação inválida!")
            return self.make_bet(current_max)