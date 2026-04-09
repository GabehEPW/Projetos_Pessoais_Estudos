class Player:

    def __init__(self, name, balance=25):
        self.name = name
        self.hand = []              # Cartas do jogador
        self.balance = balance      # Dinheiro
        self.current_bet = 0        # Aposta atual
        self.last_action = None     # ✅ Guarda última ação (IMPORTANTE!)

    def receive_card(self, card):
        # Adiciona carta na mão
        self.hand.append(card)

    def show_hand(self):
        # Mostra as cartas do jogador
        print(f"\nCartas de {self.name}:")
        for card in self.hand:
            print(f" - {card}")

    def make_bet(self, current_max):
        # Mostra informações
        print(f"\nSaldo: R${self.balance}")
        print(f"Aposta atual na mesa: R${current_max}")
        print("Escolha uma ação: check, call, raise")

        action = input("> ").lower()

        # CHECK
        if action == "check":
            if current_max > self.current_bet:
                print("Não pode dar check!")
                return self.make_bet(current_max)
            else:
                print(f"{self.name} deu check")
                self.last_action = "check"
                return 0

        # CALL
        elif action == "call":
            amount = current_max - self.current_bet
            amount = min(amount, self.balance)

            self.balance -= amount
            self.current_bet += amount

            print(f"{self.name} deu call de R${amount}")
            self.last_action = "call"
            return amount

        # RAISE
        elif action == "raise":
            while True:
                try:
                    raise_amount = int(input("Quanto deseja aumentar? R$"))
                    total = (current_max - self.current_bet) + raise_amount

                    if total > self.balance:
                        print("Saldo insuficiente!")
                    else:
                        self.balance -= total
                        self.current_bet += total

                        print(f"{self.name} deu raise de R${total}")
                        self.last_action = "raise"
                        return total
                except:
                    print("Digite um número válido!")

        # ERRO
        else:
            print("Ação inválida!")
            return self.make_bet(current_max)