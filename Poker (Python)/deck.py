import random
from card import Card  # Importa a classe Card

class Deck:

    def __init__(self):
        # Lista de naipes
        suits = ["Copas", "Espadas", "Ouros", "Paus"]

        # Lista de valores
        ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

        # Cria todas as combinações possíveis (52 cartas)
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    # Embaralha o baralho
    def shuffle(self):
        random.shuffle(self.cards)

    # Retira uma carta do topo do baralho
    def draw(self):
        return self.cards.pop()