class Card:
    # Representa UMA carta

<<<<<<< HEAD
    # Construtor da carta (executa quando cria um objeto)
    def __init__(self, suit, rank):
        self.suit = suit   # Naipe (Copas, Espadas, etc.)
        self.rank = rank   # Valor (2, 3, ..., J, Q, K, A)

    # Define como a carta será exibida no print
=======
    def __init__(self, suit, rank):
        self.suit = suit  # Naipe
        self.rank = rank  # Valor

>>>>>>> c59412fb142650a8eeaa679c97f8b507b9a69fee
    def __str__(self):
        # Como a carta aparece no print
        return f"{self.rank} de {self.suit}"