class Card:

    # Construtor da carta (executa quando cria um objeto)
    def __init__(self, suit, rank):
        self.suit = suit   # Naipe (Copas, Espadas, etc.)
        self.rank = rank   # Valor (2, 3, ..., J, Q, K, A)

    # Define como a carta será exibida no print
    def __str__(self):
        return f"{self.rank} de {self.suit}"