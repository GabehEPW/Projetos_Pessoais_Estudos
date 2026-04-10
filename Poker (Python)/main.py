from player import Player
from bot import Bot
from game import Game

# Criar jogadores
player = Player("Você")

bots = [
    Bot("Bot 1"),
    Bot("Bot 2"),
    Bot("Bot 3"),
]

players = [player] + bots

# Criar jogo
game = Game(players)

# Distribuir cartas
game.deal_cards()

# Mostrar mão do jogador
player.show_hand()

# PRÉ-FLOP
print("\n--- PRÉ-FLOP ---")
game.betting_round()

# FLOP
print("\n--- FLOP ---")
game.flop()
game.betting_round()

# TURN
print("\n--- TURN ---")
game.turn()
game.betting_round()

# RIVER
print("\n--- RIVER ---")
game.river()
game.betting_round()

print("\nFim da rodada!")