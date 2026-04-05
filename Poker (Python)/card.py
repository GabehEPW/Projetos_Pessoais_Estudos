# Classe que representa uma carta
class Card:

    # Construtor da carta
    def __init__(self, suit, rank):
        self.suit = suit   # Naipe
        self.rank = rank   # Valor

    # Define como a carta aparece ao imprimir
    def __str__(self):
        return f"{self.rank} de {self.suit}"