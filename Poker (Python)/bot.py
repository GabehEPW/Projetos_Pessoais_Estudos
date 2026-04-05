import random
from player import Player  # Bot herda Player

# Classe Bot
class Bot(Player):

    # Decide uma ação aleatória
    def make_move(self):

        action = random.choice(["fold", "call", "raise"])

        print(f"{self.name} decidiu {action}")