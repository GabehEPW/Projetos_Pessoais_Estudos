class Card:
    # Representa UMA carta

    def __init__(self, suit, rank):
        self.suit = suit  # Naipe
        self.rank = rank  # Valor

    def __str__(self):
        # Como a carta aparece no print
        return f"{self.rank} de {self.suit}"