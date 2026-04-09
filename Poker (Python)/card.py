class Card:
    # Representa UMA carta do baralho

    def __init__(self, suit, rank):
        self.suit = suit   # Naipe (Copas, Espadas...)
        self.rank = rank   # Valor (2, 3, J, A...)

    def __str__(self):
        # Define como a carta aparece ao dar print()
        return f"{self.rank} de {self.suit}"