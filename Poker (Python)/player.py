class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    # Recebe uma carta
    def receive_card(self, card):
        self.hand.append(card)

    # Mostra as cartas do jogador
    def show_hand(self):

        print(f"\nCartas de {self.name}:")

        for card in self.hand:
            print(card)