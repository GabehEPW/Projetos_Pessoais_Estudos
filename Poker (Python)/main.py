from deck import Deck
from player import Player
from bot import Bot

# Criar e embaralhar baralho
deck = Deck()
deck.shuffle()

initial_balance = 25

# Criar jogador
player = Player("Jogador", balance=initial_balance)

# Criar bots
bots = [
    Bot("Bot 1", balance=initial_balance),
    Bot("Bot 2", balance=initial_balance),
    Bot("Bot 3", balance=initial_balance),
    Bot("Bot 4", balance=initial_balance)
]

players = [player] + bots

# Distribuir 2 cartas para cada jogador
for _ in range(2):
    for p in players:
        p.receive_card(deck.draw())

# Mostrar cartas do jogador
player.show_hand()

# Rodada de apostas
current_max = 0

bet = player.make_bet(current_max)
player_action = player.last_action  # ✅ agora funciona

# Atualiza maior aposta
if player.current_bet > current_max:
    current_max = player.current_bet

# Bots jogam
for bot in bots:
    bet, action = bot.make_move(current_max, player_action)

    if bot.current_bet > current_max:
        current_max = bot.current_bet

# Mostrar saldo final
print("\nSaldo após a rodada:")
for p in players:
    print(f"{p.name}: R${p.balance}")