from deck import Deck
from player import Player
from bot import Bot
from hand_evaluator import evaluate_hand  # 🔥 novo

# Criação inicial
initial_balance = 25

player = Player("Jogador", balance=initial_balance)

bots = [
    Bot("Bot 1", balance=initial_balance),
    Bot("Bot 2", balance=initial_balance),
    Bot("Bot 3", balance=initial_balance),
    Bot("Bot 4", balance=initial_balance)
]

players = [player] + bots


# 🔁 LOOP PRINCIPAL DO JOGO
while True:

    print("\n===== NOVA RODADA =====")

    # Cria e embaralha baralho
    deck = Deck()
    deck.shuffle()

    # Reset dos jogadores
    for p in players:
        p.hand = []
        p.current_bet = 0
        p.last_action = None

    pot = 0
    current_max = 0

    # Distribui 2 cartas para cada jogador
    for _ in range(2):
        for p in players:
            p.receive_card(deck.draw())

    # Mostra cartas do jogador
    player.show_hand()

    # 🔥 Mostra a força da mão
    hand_name, strength = evaluate_hand(player.hand)
    print(f"Sua mão: {hand_name}")

    # Lista de jogadores ativos (quem não foldou)
    active_players = players.copy()

    # 🔁 LOOP DE APOSTAS (até todos igualarem)
    while True:
        all_matched = True

        for p in active_players[:]:  # cópia da lista

            # Jogador humano
            if isinstance(p, Player) and not isinstance(p, Bot):
                bet, action = p.make_bet(current_max)

            # Bots
            else:
                bet, action = p.make_move(
                    current_max,
                    player.last_action if player.last_action else "check"
                )

            pot += bet

            # Se aumentou aposta → todos precisam responder
            if p.current_bet > current_max:
                current_max = p.current_bet
                all_matched = False

            # Se desistiu (fold)
            if action == "fold":
                active_players.remove(p)

            # Se só sobrou um → vitória automática
            if len(active_players) == 1:
                winner = active_players[0]
                winner.balance += pot
                print(f"\n🏆 {winner.name} ganhou o pote de R${pot} (todos desistiram)")
                break

        if len(active_players) == 1:
            break

        # Verifica se todos igualaram aposta
        for p in active_players:
            if p.current_bet != current_max:
                all_matched = False

        if all_matched:
            break

    # 🔥 Definição de vencedor (TEMPORÁRIO)
    if len(active_players) > 1:
        winner = active_players[0]  # simplificado
        winner.balance += pot
        print(f"\n🏆 {winner.name} ganhou o pote de R${pot}")

    # Mostra saldo
    print("\nSaldo atual:")
    for p in players:
        print(f"{p.name}: R${p.balance}")

    # Verifica se alguém venceu o jogo inteiro
    alive = [p for p in players if p.balance > 0]

    if len(alive) == 1:
        print(f"\n🏆 {alive[0].name} venceu o jogo!")
        break

    # Pergunta se quer continuar
    cont = input("\nJogar outra rodada? (s/n): ").lower()
    if cont != "s":
        break