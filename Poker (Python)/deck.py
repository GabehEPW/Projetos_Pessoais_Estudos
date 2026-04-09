import random
from card import Card

class Deck:
    # Representa o baralho completo

    def __init__(self):
        suits = ["Copas", "Espadas", "Ouros", "Paus"]
        ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

        # Cria TODAS as combinações de cartas
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        # Embaralha as cartas
        random.shuffle(self.cards)

    def draw(self):
        # Remove e retorna a última carta do baralho
        return self.cards.pop()