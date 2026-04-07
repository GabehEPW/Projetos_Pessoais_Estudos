from deck import Deck
from player import Player
from bot import Bot

# Cria o baralho e embaralha
deck = Deck()
deck.shuffle()

# Saldo inicial
initial_balance = 25

# Cria jogador com saldo
player = Player("Jogador", balance=initial_balance)

# Cria bots com saldo
bots = [
    Bot("Bot 1", balance=initial_balance),
    Bot("Bot 2", balance=initial_balance),
    Bot("Bot 3", balance=initial_balance),
    Bot("Bot 4", balance=initial_balance)
]

players = [player] + bots

# Cada jogador recebe 2 cartas
for _ in range(2):
    for p in players:
        p.receive_card(deck.draw())

# Mostra as cartas do jogador
player.show_hand()

# Variáveis de apostas
current_max = 0           # maior aposta na mesa
player_action = "check"   # última ação do jogador

# Rodada de apostas
bet = player.make_bet(current_max)
player_action = player.last_action  # salva a última ação do jogador
if player.current_bet > current_max:
    current_max = player.current_bet

for bot in bots:
    bet, action = bot.make_move(current_max, player_action)
    if bot.current_bet > current_max:
        current_max = bot.current_bet

# Mostra saldo final após a rodada
print("\nSaldo após a rodada:")
for p in players:
    print(f"{p.name}: R${p.balance}")