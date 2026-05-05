from collections import Counter

# Ordem das cartas (IMPORTANTE para comparação futura)
RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
}

def evaluate_hand(cards):
    ranks = [card.rank for card in cards]
    suits = [card.suit for card in cards]

    rank_counts = Counter(ranks)
    values = sorted([RANK_VALUES[r] for r in ranks])

    # Quantidade de repetições
    counts = sorted(rank_counts.values(), reverse=True)

    # Verifica flush (mesmo naipe)
    is_flush = len(set(suits)) == 1

    # Verifica sequência
    is_straight = False
    if len(values) >= 5:
        for i in range(len(values) - 4):
            if values[i:i+5] == list(range(values[i], values[i] + 5)):
                is_straight = True

    # 🔥 Ranking das mãos (do mais forte pro mais fraco)

    if is_straight and is_flush:
        return "Straight Flush", 8

    elif 4 in counts:
        return "Quadra (4 iguais)", 7

    elif 3 in counts and 2 in counts:
        return "Full House", 6

    elif is_flush:
        return "Flush", 5

    elif is_straight:
        return "Sequência", 4

    elif 3 in counts:
        return "Trinca", 3

    elif counts.count(2) >= 2:
        return "Dois Pares", 2

    elif 2 in counts:
        return "Um Par", 1

    else:
        return "Carta Alta", 0