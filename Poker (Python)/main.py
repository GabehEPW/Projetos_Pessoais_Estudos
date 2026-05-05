from deck import Deck
from player import Player
from bot import Bot

# Inicialização
deck = Deck()
deck.shuffle()

initial_balance = 25

player = Player("Jogador", balance=initial_balance)

bots = [
    Bot("Bot 1", balance=initial_balance),
    Bot("Bot 2", balance=initial_balance),
    Bot("Bot 3", balance=initial_balance),
    Bot("Bot 4", balance=initial_balance)
]

players = [player] + bots


# 🔁 LOOP DO JOGO (várias rodadas)
while True:

    print("\n===== NOVA RODADA =====")

    # Reset da rodada
    deck = Deck()
    deck.shuffle()

    for p in players:
        p.hand = []
        p.current_bet = 0

    pot = 0
    current_max = 0

    # Distribui cartas
    for _ in range(2):
        for p in players:
            p.receive_card(deck.draw())

    player.show_hand()

    active_players = players.copy()

    # 🔥 LOOP DE APOSTAS (ESSENCIAL)
    while True:
        all_matched = True

        for p in active_players[:]:  # cópia da lista

            # Jogador humano
            if isinstance(p, Player) and not isinstance(p, Bot):
                bet, action = p.make_bet(current_max)
            else:
                bet, action = p.make_move(current_max, player.last_action if player.last_action else "check")

            pot += bet

            # Se aumentou aposta → todos precisam jogar de novo
            if p.current_bet > current_max:
                current_max = p.current_bet
                all_matched = False

            # Se foldou → remove da rodada
            if action == "fold":
                active_players.remove(p)

            # Se sobrou só 1 jogador → ganha direto
            if len(active_players) == 1:
                winner = active_players[0]
                winner.balance += pot
                print(f"\n🏆 {winner.name} ganhou o pote de R${pot} (todos foldaram)")
                break

        if len(active_players) == 1:
            break

        # Verifica se todos igualaram aposta
        for p in active_players:
            if p.current_bet != current_max:
                all_matched = False

        if all_matched:
            break

    # 🔥 Definir vencedor (simplificado por enquanto)
    if len(active_players) > 1:
        winner = active_players[0]  # simplificação
        winner.balance += pot
        print(f"\n🏆 {winner.name} ganhou o pote de R${pot}")

    # Mostrar saldo
    print("\nSaldo atual:")
    for p in players:
        print(f"{p.name}: R${p.balance}")

    # Condição de fim
    alive = [p for p in players if p.balance > 0]

    if len(alive) == 1:
        print(f"\n🏆 {alive[0].name} venceu o jogo!")
        break

    # Pergunta se continua
    cont = input("\nJogar outra rodada? (s/n): ").lower()
    if cont != "s":
        break