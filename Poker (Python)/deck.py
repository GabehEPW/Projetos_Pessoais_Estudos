import random
<<<<<<< HEAD
from card import Card  # Importa a classe Card
=======
from card import Card
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee

class Deck:
    # Representa o baralho completo

    def __init__(self):
<<<<<<< HEAD
        # Lista de naipes
=======
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
        suits = ["Copas", "Espadas", "Ouros", "Paus"]

        # Lista de valores
        ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

<<<<<<< HEAD
        # Cria todas as combinações possíveis (52 cartas)
=======
        # Cria todas as cartas
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        # Embaralha
        random.shuffle(self.cards)

<<<<<<< HEAD
    # Retira uma carta do topo do baralho
=======
>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
    def draw(self):
        # Retira uma carta do topo
        return self.cards.pop()