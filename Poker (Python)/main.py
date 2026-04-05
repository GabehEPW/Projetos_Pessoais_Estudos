from deck import Deck
from player import Player
from bot import Bot


# Cria o baralho
deck = Deck()

# Embaralha
deck.shuffle()


# Cria jogador
player = Player("Jogador")


# Cria bots
bots = [
    Bot("Bot 1"),
    Bot("Bot 2"),
    Bot("Bot 3"),
    Bot("Bot 4")
]


# Cada jogador recebe 2 cartas
for i in range(2):

    player.receive_card(deck.draw())

    for bot in bots:
        bot.receive_card(deck.draw())


# Mostra cartas do jogador
player.show_hand()


# Bots fazem jogadas
for bot in bots:
    bot.make_move()