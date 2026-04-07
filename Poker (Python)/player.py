# Classe jogador
class Player:

    def __init__(self, name, balance=25):
        self.name = name
        self.hand = []
        self.balance = balance   # saldo do jogador
        self.current_bet = 0     # aposta atual na rodada

    # Recebe uma carta
    def receive_card(self, card):
        self.hand.append(card)

    # Mostra as cartas do jogador
    def show_hand(self):
        print(f"\nCartas de {self.name}:")
        for card in self.hand:
            print(card)

    # Jogador faz uma aposta
    def make_bet(self, current_max):
        print(f"\nSaldo: R${self.balance}")
        print(f"Aposta atual na mesa: R${current_max}")
        print("Escolha uma ação: check, call, raise")
        
        action = input("> ").lower()

        # Check → passa a vez se já não houver aposta
        if action == "check":
            if current_max > self.current_bet:
                print("Não pode dar check, precisa dar call ou raise!")
                return self.make_bet(current_max)
            else:
                print(f"{self.name} deu check")
                return 0

        # Call → iguala a maior aposta
        elif action == "call":
            amount = current_max - self.current_bet
            if amount > self.balance:
                amount = self.balance  # aposta tudo que tem
            self.balance -= amount
            self.current_bet += amount
            print(f"{self.name} deu call de R${amount}")
            return amount

        # Raise → aumenta a aposta
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
                        return total
                except:
                    print("Digite um número válido!")
        else:
            print("Ação inválida!")
            return self.make_bet(current_max)