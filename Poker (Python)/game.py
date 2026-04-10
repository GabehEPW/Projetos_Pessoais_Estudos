from deck import Deck

class Game:

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.table_cards = []
        self.current_max = 0

    def show_table(self):
        print("\nCartas na mesa:")
        for c in self.table_cards:
            print(f" - {c}")

    def deal_cards(self):
        # Embaralha e distribui 2 cartas
        self.deck.shuffle()

        for _ in range(2):
            for p in self.players:
                p.receive_card(self.deck.draw())

    def betting_round(self):
        # Loop de apostas
        while True:
            all_equal = True

            for p in self.players:

                if not p.active:
                    continue

                if hasattr(p, "make_bet"):
                    p.make_bet(self.current_max)
                    action = p.last_action
                else:
                    _, action = p.make_move(self.current_max)

                # Se desistiu
                if action == "fold":
                    continue

                # Atualiza maior aposta
                if p.current_bet > self.current_max:
                    self.current_max = p.current_bet
                    all_equal = False

                elif p.current_bet < self.current_max:
                    all_equal = False

            if all_equal:
                break

    def flop(self):
        # 3 cartas
        for _ in range(3):
            self.table_cards.append(self.deck.draw())

        self.show_table()

    def turn(self):
        # 1 carta
        self.table_cards.append(self.deck.draw())
        self.show_table()

    def river(self):
        # 1 carta
        self.table_cards.append(self.deck.draw())
        self.show_table()