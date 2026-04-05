import random
from card import Card   # Importa a classe Card

class Deck:

    def __init__(self):

        suits = ["Copas", "Espadas", "Ouros", "Paus"]
        ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

        self.cards = []

        # Cria todas as cartas
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    # Embaralha o baralho
    def shuffle(self):
        random.shuffle(self.cards)

    # Puxa uma carta do baralho
    def draw(self):
        return self.cards.pop()